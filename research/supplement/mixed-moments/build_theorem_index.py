#!/usr/bin/env python3
"""Original metadata writer and dependency-DAG validator; standard library only."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SOURCE=ROOT/'catalog'/'sources'/'preprints_Catalans-constant-is-irrational-September-24-2026_build_sections_foundations.tex'
REVISION='fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'
URL=f'https://github.com/openai/math/blob/{REVISION}/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex'
records=[]

def theorem(id,title,hypotheses,conclusion,dependencies,section,source_labels=None,source_lines=None,kind='source-supported theorem with independent proof'):
    records.append({'id':id,'title':title,'hypotheses':hypotheses,'conclusion':conclusion,
                    'dependencies':dependencies,'proof':{'file':'study.md','section':section,'status':'ordinary mathematical proof provided; not Lean verified'},
                    'source':{'labels':source_labels or [],'line_range':source_lines},'kind':kind})

theorem('MM001','Absolute integrability of M',
        ['P and Q are real polynomials','f(t) is the positive square root of 1-t^2 for -1<t<1'],
        'The absolute integral of |t| P(t) Q(s) / (f(t)(1-ts)) over (-1,1) x (0,1) is finite; both integration orders agree.',
        [],'2',['eq:mixed-moments'],[54,71])
theorem('MM002','Absolute integrability of Z',
        ['D and Q are real polynomials'],
        'The absolute integral of D(t) Q(s)/(1-ts) over (0,1)^2 is finite; both integration orders agree.',
        [],'2',['eq:mixed-moments'],[54,71])
theorem('MM003','Central binomial recurrence and generating series',
        ['c_r = binomial(2r,r)/4^r for natural r'],
        'c_0=1; c_(r+1)=((2r+1)/(2r+2))*c_r; sum_(r>=0) c_r*t^(2r)=1/sqrt(1-t^2) for |t|<1.',
        [],'3',['eq:moment-values'],[95,105])
theorem('MM004','Rational one variable moments',
        ['i is a nonnegative integer','m_i is the integral of |t|t^i/f(t)','m_(-1) is defined as 0'],
        'm_i=0 for odd i and 2/((i+1)c_(i/2)) for even i; (i+1)m_i=i*m_(i-2) for i>=1; m_i tends to 0.',
        ['MM001','MM003'],'4',['eq:moment-values'],[95,105])
theorem('MM005','M moment series',
        ['i,j are nonnegative integers'],
        'M(i,j)=sum_(u>=0) m_(i+u)/(j+u+1), with absolute justification of the signed geometric expansion.',
        ['MM001','MM004'],'6',['eq:moment-series'],[106,110])
theorem('MM006','M diagonal recurrence and reduction',
        ['i,j are nonnegative integers'],
        'M(i,j)-M(i+1,j+1)=m_i/(j+1); finite iteration gives the two diagonal-reduction formulas in study.md section 6.',
        ['MM005'],'6',['eq:moment-series','eq:diagonal-reduction'],[107,183])
theorem('MM007','Harmonic evaluation of Z',
        ['i,j are nonnegative integers','H_n=sum_(k=1..n)1/k','H_n^(2)=sum_(k=1..n)1/k^2'],
        'Z(i,i)=zeta(2)-H_i^(2); for i!=j, Z(i,j)=(H_i-H_j)/(i-j).',
        ['MM002'],'5',['eq:rational-z','eq:rational-decomposition'],[190,211])
theorem('MM008','M boundary recurrences',
        ['Kminus_d=M(d,0)','Kplus_d=M(0,d)','d>=2 is an integer'],
        'd*Kminus_d=(d-1)*Kminus_(d-2)+m_(d-2)+m_(d-1); Kminus_1=2; (d-1)*Kplus_d=(d-2)*Kplus_(d-2)+2/(d-1).',
        ['MM004','MM005'],'7',['eq:boundary-recurrences'],[112,133])
theorem('MM009','Catalan boundary start',
        ['G=sum_(r>=0)(-1)^r/(2r+1)^2'],
        'M(0,0)=4G.',
        ['MM001'],'8 Catalan start',['eq:boundary-starts'],[135,146])
theorem('MM010','Zeta boundary start',
        ['zeta(2)=sum_(n>=1)1/n^2'],
        'M(0,1)=(3/2)*zeta(2), by the nonnegative integral -2*integral_0^1 log(x)/(1-x^2) dx.',
        ['MM001'],'8 zeta start',['eq:boundary-starts'],[135,166],kind='source result; shorter independent direct-integral proof')
theorem('MM011','Optional pi evaluation',
        ['pi and arcsin have their usual real analytic meanings'],
        'M(0,1)=pi^2/4 and hence zeta(2)=pi^2/6.',
        ['MM003','MM004','MM005','MM010'],'8 pi notation',['eq:boundary-starts'],[147,166])
theorem('MM012','Rational boundary arrays and closed forms',
        ['kminus_0=kplus_0=kplus_1=0','kminus_1=2','the arrays satisfy the source boundary recurrences','Hstar_z=c_(z/2) for even z and 1/(z*c_((z-1)/2)) for odd z'],
        'The arrays are uniquely rational; Hstar_(z+2)/Hstar_z=(z+1)/(z+2); the three finite closed-form sums in study.md section 9 hold, including empty sums.',
        ['MM003','MM004'],'9',['eq:rational-starts','eq:h-star','eq:explicit-boundary-arrays'],[168,241])
theorem('MM013','Universal M decomposition',
        ['i,j are nonnegative integers','M0 is the rational diagonal-reduction array','c_(a/2)=0 if the integer a is negative or odd'],
        'M(i,j)=M0(i,j)+4G*c_((i-j)/2)+(3/2)*zeta(2)*c_((j-i-1)/2). No uniqueness or independence of real constants is asserted.',
        ['MM003','MM006','MM008','MM009','MM010','MM012'],'10',['eq:rational-decomposition'],[168,207])
theorem('MM014','Exact polynomial defect identity',
        ['P,D are rational polynomials','j is a nonnegative integer','p_i,d_i are their coefficients'],
        'M(P,j)-(3/2)Z(D,j)=A_j+B_j*G+(3/2)*E_j*zeta(2), with A_j=sum_i p_i*M0(i,j)-(3/2)*sum_i d_i*Z0(i,j), B_j=4*sum_(r>=0)p_(j+2r)c_r, E_j=[t^j](tP/sqrt(1-t^2)-D).',
        ['MM003','MM007','MM013'],'11',['eq:rational-decomposition','eq:rational-raw-entry'],[197,261],kind='generalized reusable extraction with independent proof')
theorem('MM015','Analytic contact and finite jet vanishing',
        ['F is analytic in a real neighborhood of zero','L is a nonnegative integer'],
        'F(t)=O(t^L) as t tends to zero iff its Taylor coefficients in degrees less than L vanish; one-sided contact suffices as well.',
        [],'11',kind='elementary auxiliary theorem')
theorem('MM016','Rational polynomial Taylor contact cancellation',
        ['P,D are rational polynomials','L>=1 is an integer','tP(t)/sqrt(1-t^2)-D(t)=O(t^L) as t tends to zero','j is an integer with 0<=j<L'],
        'There are explicitly specified rational A_j,B_j such that M(P,j)-(3/2)Z(D,j)=A_j+B_j*G.',
        ['MM014','MM015'],'11',['eq:contact','prop:rationality'],[243,262],kind='main generalized extraction; ordinary proof completed')
theorem('MM017','Polynomial test function cancellation',
        ['P,D,Q are rational polynomials','the finite pairing sum_j coefficient(Q,j)*E_j equals zero'],
        'M(P,Q)-(3/2)Z(D,Q) belongs to Q+QG. In particular contact of order L and degree(Q)<L imply this conclusion.',
        ['MM014','MM015'],'12 Polynomial test functions',kind='bilinear reusable corollary')
theorem('MM018','Unique contact truncation',
        ['P is a rational polynomial','L>=1 is an integer'],
        'The unique degree-less-than-L D with contact order at least L is the degree-less-than-L truncation of tP/sqrt(1-t^2). All polynomial solutions differ from it by a multiple of t^L.',
        ['MM003','MM015'],'12 Computing a matching polynomial',kind='constructive reusable corollary')
theorem('MM019','Exact rational series tail bound',
        ['i,j are nonnegative integers','N>=1 is an integer'],
        'The tail after N terms of the M series lies between zero and max(1,(i+N)/(j+N+1))*(m_(i+N-2)+m_(i+N-1)).',
        ['MM004','MM005'],'6 Exact rational tail bound',kind='additional reusable estimate')
theorem('MM020','Rational adjacent diagonal',
        ['i>=1 is an integer'],
        'M(i,i-1)=m_(i-2)+m_(i-1).',
        ['MM004','MM005'],'6 Exact rational tail bound',kind='additional telescoping identity')
theorem('MM021','Coefficient field extension',
        ['K is a subfield of R','P,D have coefficients in K','the same integer-index and Taylor-contact hypotheses as MM016 hold'],
        'M(P,j)-(3/2)Z(D,j) belongs to K+K*G.',
        ['MM003','MM007','MM013','MM015'],'12 Other coefficient fields',kind='same proof with coefficient field generalized')

ids={r['id'] for r in records}
assert len(ids)==len(records)
for r in records:
    assert all(d in ids for d in r['dependencies'])
by_id={r['id']:r for r in records}
seen=set(); active=set(); order=[]
def visit(id):
    if id in seen:return
    assert id not in active, 'dependency cycle'
    active.add(id)
    for d in by_id[id]['dependencies']:visit(d)
    active.remove(id);seen.add(id);order.append(id)
for id in by_id:visit(id)

manifest=json.loads((ROOT/'catalog'/'source_manifest.json').read_text())
source_hash=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
source_entry=next(x for x in manifest['files'] if x['file']==SOURCE.name)
assert source_hash==source_entry['sha256']

payload={
 'schema_version':1,'study':'Family005 mixed moments and Taylor-contact cancellation',
 'source':{'repository':'https://github.com/openai/math','revision':REVISION,
           'path':'preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex',
           'url':URL,'local_snapshot':str(SOURCE),'sha256':source_hash,
           'matches_catalog_manifest':True,'scoped_lines':[[54,71],[93,262]],
           'exclusions':['two-adic valuation subsection','determinant nonvanishing','Catalan irrationality']},
 'conventions':{'domains':'i,j are nonnegative integers unless an extension is stated explicitly',
                'square_root':'positive on (-1,1)',
                'central_kernel':'c_(a/2)=0 for negative or odd integer a',
                'negative_moment':'m_(-1)=0 only as an explicit convention in recurrences',
                'formal_coordinates':['1','G','zeta(2)'],
                'no_independence_assumption':True,
                'polynomial_coefficients':'rational in the main theorem'},
 'theorems':records,'topological_order':order,
 'verification':{'ordinary_mathematical_proofs':'study.md','independent_audit':'audit.md',
                 'exact_arithmetic_program':'certificates.py','exact_arithmetic_output':'certificates.json',
                 'test_scope':'Finite exact identities only; no substitution for G or zeta(2)',
                 'lean_compiled':False,'lean_declarations_matched':False,
                 'external_code_executed':False,'original_standard_library_code_executed':True},
 'nonclaims':['No proof of Catalan irrationality','No claim of independence of 1, G, zeta(2)',
              'No unconditional nonmembership conclusion from a nonzero formal zeta(2) coordinate',
              'No Lean verification or compilation claim','No validation of later manuscript sections']}
(HERE/'theorems.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'theorems':len(records),'dependency_edges':sum(len(r['dependencies']) for r in records),
                  'dag_validated':True,'source_matches_catalog':True},indent=2))
