from pathlib import Path
import hashlib,json,re,subprocess,sys
p=Path(__file__).resolve().parent.parent
if sys.argv[1]=='pins':
 for name,expected in {
  'lean-toolchain':'42779d67b81608af8a12aa4328d2ab47ca201925b3b2bd68369587b5340bb434',
  'lakefile.toml':'8a0795707a9dfe1849a315b5c4295c81ae017ad372a7944464fa1cb01eaa186a',
  'lake-manifest.json':'b944c3b78c23f888779246046dcb33f0d3e3483470ee200e2732a51ef68c49ad'
 }.items():
  h=hashlib.sha256((p/name).read_bytes()).hexdigest();assert h==expected,(name,h);print('PIN',name,h)
 version=subprocess.check_output(['lean','--version'],text=True)
 assert 'version 4.24.0,' in version and '797c613eb9b6d4ec95db23e3e00af9ac6657f24b' in version
 for pkg in json.loads((p/'lake-manifest.json').read_text())['packages']:
  h=subprocess.check_output(['git','-C',str(p/'.lake/packages'/pkg['name']),'rev-parse','HEAD'],text=True).strip()
  assert h==pkg['rev'];print('DEPENDENCY',pkg['name'],h)
 print('PASS exact compiler and all nine dependency pins')
else:
 names=json.loads((p/'evidence/declaration-inventory.json').read_text())
 for f in [p/'ConvexApprox.lean',*sorted((p/'ConvexApprox').glob('*.lean'))]:
  text=f.read_text()
  assert not re.search(r'\b(sorry|admit|axiom)\b',text),f
  print('SOURCE',f.relative_to(p),hashlib.sha256(f.read_bytes()).hexdigest())
 log=(Path(sys.argv[2]) if len(sys.argv)>2 else p/'logs/final-type-axiom-audit.log').read_text()
 assert 'sorryAx' not in log and 'error:' not in log
 groups=re.findall(r'depends on axioms: \[([^\]]*)\]',log)
 ax={s.strip() for g in groups for s in g.split(',') if s.strip()}
 no_axioms=len(re.findall(r'does not depend on any axioms',log))
 assert len(groups)+no_axioms==len(names),(len(groups),no_axioms,len(names))
 assert ax<={'propext','Classical.choice','Quot.sound'},ax
 print('PASS all',len(names),'project declarations inspected; axioms:',sorted(ax))
 print('PASS no placeholders or new project axioms')
 print('EXIT: 0')
