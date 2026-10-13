#!/usr/bin/env python3
"""Inspect the staged scoped publication; print evidence without secret values.

Run after git add transport-sharpness, before committing. This does not publish,
change credentials, or modify files. Pattern inspection is accompanied by the
manual privacy/license review documented in docs/SOURCES.md.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

BASELINE = 'b1d6c20e2f02b484d09c5285e67d842b369f9df0'
BRANCH = 'codex/transport-sharpness-2026-10-13'
PREFIX = 'transport-sharpness/'
ROOT = Path(__file__).resolve().parents[2]
PATTERNS = {
    'github_token': r'\b(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,})\b',
    'api_secret': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b',
    'aws_access_key': r'\b(?:AKIA|ASIA)[0-9A-Z]{16}\b',
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'credential_url': r'https?://[^/\s:@]+:[^/@\s]+@',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode().strip()


def strict_object(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON object key: ' + key)
        out[key] = value
    return out


def main():
    require(git('branch', '--show-current') == BRANCH, 'wrong publication branch')
    subprocess.run(['git', 'merge-base', '--is-ancestor', BASELINE, 'HEAD'], cwd=ROOT, check=True)
    changes = [line.split('\t') for line in git('diff', '--cached', '--name-status', BASELINE).splitlines()]
    require(bool(changes), 'there is no staged task publication')
    require(all(len(row) == 2 and row[0] == 'A' and row[1].startswith(PREFIX)
                for row in changes), 'publication changes must only add scoped paths')
    require(not git('diff', '--name-only'), 'unstaged tracked changes require inspection')
    require(not git('diff', BASELINE, '--', '.', ':!transport-sharpness'), 'prior files changed')
    for args in (['diff', '--check'], ['diff', '--cached', '--check']):
        subprocess.run(['git', *args], cwd=ROOT, check=True)
    indexed = git('ls-files', PREFIX).splitlines()
    require(indexed, 'no indexed scoped files')
    records = []
    json_count = 0
    for name in indexed:
        path = ROOT / name
        require(path.is_file() and not path.is_symlink(), 'nonregular published path: ' + name)
        require(not any(part in {'.lake', '.cache', '.elan', '__pycache__'} for part in path.parts),
                'cache path must be excluded: ' + name)
        require(path.suffix not in {'.olean', '.ilean', '.pyc', '.zip', '.zst', '.so'},
                'compiled product or archive must be excluded: ' + name)
        data = path.read_bytes()
        text = data.decode('utf-8')
        for label, pattern in PATTERNS.items():
            require(not re.search(pattern, text), 'potential ' + label + ' in ' + name)
        if path.suffix == '.json':
            json.loads(text, object_pairs_hook=strict_object)
            json_count += 1
        records.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    lock = json.loads((ROOT / PREFIX / 'lake-manifest.json').read_text())
    baseline_lock = json.loads(git('show', BASELINE + ':tangent-limit/lake-manifest.json'))
    require(lock['packages'] == baseline_lock['packages'] and len(lock['packages']) == 9,
            'dependency lock differs from saved official package pins')
    require((ROOT / PREFIX / 'lean-toolchain').read_text().strip() == 'leanprover/lean4:v4.24.0',
            'Lean toolchain differs from pin')
    print(json.dumps({'schema': 'transport-sharpness-publication-preflight/v1',
                      'checked_utc': datetime.now(timezone.utc).isoformat(),
                      'branch': BRANCH, 'baseline': BASELINE,
                      'status': 'passed', 'scoped_added_files': len(changes),
                      'indexed_file_count': len(indexed), 'strict_json_count': json_count,
                      'secret_pattern_names': sorted(PATTERNS), 'secret_pattern_matches': 0,
                      'privacy_review': 'manual mathematical/log inspection plus listed patterns; no claim of a general secret detector',
                      'license_review': 'existing attribution inspected; no third-party source or cache redistributed; no new overall license assigned',
                      'prior_tracked_files_unchanged': True,
                      'dependency_lock_matches_baseline': True,
                      'files': records}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
