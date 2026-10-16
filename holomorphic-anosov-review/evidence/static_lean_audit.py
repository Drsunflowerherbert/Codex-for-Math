#!/usr/bin/env python3
"""Bounded lexical audit, not Lean elaboration or theorem verification.

Erases nested comments and strings while retaining newlines, scans noteworthy
tokens, and computes local module import reachability from explicit roots.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path


def erase_noncode(source):
    out = list(source)
    i, depth = 0, 0
    while i < len(source):
        if depth:
            if source.startswith('/-', i):
                out[i:i+2] = '  '; depth += 1; i += 2
            elif source.startswith('-/', i):
                out[i:i+2] = '  '; depth -= 1; i += 2
            else:
                if source[i] != '\n': out[i] = ' '
                i += 1
        elif source.startswith('/-', i):
            out[i:i+2] = '  '; depth = 1; i += 2
        elif source.startswith('--', i):
            j = source.find('\n', i)
            if j < 0: j = len(source)
            out[i:j] = ' ' * (j-i); i = j
        elif source[i] == '"':
            out[i] = ' '; i += 1
            while i < len(source):
                c = source[i]
                if c != '\n': out[i] = ' '
                i += 1
                if c == '\\' and i < len(source):
                    if source[i] != '\n': out[i] = ' '
                    i += 1
                elif c == '"': break
        else:
            raw = re.compile(r'r(#+)"').match(source, i) if source[i] == 'r' else None
            if raw:
                endmark = '"' + raw.group(1)
                j = source.find(endmark, raw.end())
                j = len(source) if j < 0 else j + len(endmark)
                for k in range(i, j):
                    if source[k] != '\n': out[k] = ' '
                i = j
            else: i += 1
    if depth: raise ValueError('Unclosed block comment')
    return ''.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('repository', type=Path)
    ap.add_argument('output', type=Path)
    args = ap.parse_args()
    base = args.repository.resolve()
    # Checks protect against the false-positive class that motivated this scan.
    assert 'sorry' not in erase_noncode('/- a /- sorry -/ b -/ -- sorry\n"sorry"')
    assert erase_noncode('/- a\nb -/\nsorry').count('\n') == 2
    assert 'sorry' in erase_noncode('/- a -/ by sorry')
    files = sorted(base.rglob('*.lean'))
    modules, noteworthy, declarations, imports = {}, [], [], {}
    tokens = re.compile(r'\b(sorryAx|sorry|admit|axiom|unsafe|opaque|implemented_by|extern|run_cmd|initialize)\b')
    decl = re.compile(r'^\s*(?:(?:private|protected|noncomputable|unsafe)\s+)*(theorem|lemma|def|abbrev|structure|class|axiom|opaque)\s+([^\s:{(]+)', re.M)
    for path in files:
        rel = path.relative_to(base).as_posix()
        module = rel[:-5].replace('/', '.')
        source = path.read_text()
        code = erase_noncode(source)
        modules[module] = {'path': rel, 'lines': len(source.splitlines()),
                           'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        imports[module] = []
        for m in re.finditer(r'^\s*(?:public\s+)?import\s+([^\n]+)', code, re.M):
            imports[module].extend(m.group(1).split())
        for m in tokens.finditer(code):
            noteworthy.append({'path': rel, 'line': code.count('\n', 0, m.start())+1,
                               'token': m.group(1)})
        for m in decl.finditer(code):
            declarations.append({'path': rel, 'line': code.count('\n', 0, m.start())+1,
                                 'kind': m.group(1), 'name': m.group(2)})
    roots = ['Comparator.Solution', 'HolomorphicAnosov.Targets.TheoremA',
             'HolomorphicAnosov.Targets.Theorem11', 'HolomorphicAnosov.Targets.Theorem12',
             'HolomorphicAnosov.Targets.Theorem13']
    closures = {}
    for root in roots:
        seen, external, todo = set(), set(), [root]
        while todo:
            module = todo.pop()
            if module in seen: continue
            if module not in modules: external.add(module); continue
            seen.add(module); todo.extend(imports[module])
        reached = {modules[m]['path'] for m in seen}
        closures[root] = {'local_module_count': len(seen), 'local_modules': sorted(seen),
                          'external_imports': sorted(external),
                          'noteworthy': [x for x in noteworthy if x['path'] in reached],
                          'imports_challenge': 'Comparator.Challenge' in seen}
    result = {'method': 'Lexical source scan and module import closure only; no Lean elaboration, no declaration-level proof dependency or kernel axiom verification.',
              'lean_file_count': len(files), 'source_lines': sum(v['lines'] for v in modules.values()),
              'noteworthy': noteworthy, 'module_data': modules, 'imports': imports,
              'declarations': declarations, 'closures': closures}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'files': len(files), 'lines': result['source_lines'],
                      'noteworthy': noteworthy,
                      'closures': {r: {k:v for k,v in d.items() if k not in ['local_modules','external_imports']} for r,d in closures.items()}}, indent=2))


if __name__ == '__main__': main()
