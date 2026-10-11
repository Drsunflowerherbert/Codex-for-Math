# Separate refinements of the finite affine transport calculation

These are ordinary mathematical deductions checked during the independent review. They have their own hypotheses and do not silently weaken or replace the original theorem records. No novelty or formal-verification claim is made.

## Fixed priority gives a unique induced optimal plan without source regularity

### Statement

Let rho be any Borel probability measure on R^d with finite second moment. Let u(x)=max_i(x·y_i+c_i) be a nonempty finite affine maximum with finite real intercepts. No absolute continuity is assumed.

Merge repeated slopes by keeping the largest intercept for each slope. On the remaining distinct slopes, choose any one fixed total order, independent of x. Define T(x) to be the earliest maximizing slope in this order, and let lambda=T#rho. Then T is Borel and (id,T)#rho is the unique quadratic-cost optimal plan from rho to this induced target lambda.

The statement does not assert T=gradient(u) rho-almost everywhere. That additional conclusion holds if the active distinct-slope tie set is rho-null, in particular under the original null-hyperplane or absolute-continuity hypothesis.

### Relation to the original first-index rule

To preserve the original rule exactly when slopes repeat, retain for each slope its largest intercept and assign it the least original index among copies having that largest intercept. Order the distinct retained slopes by these indices. Copies with a smaller intercept can never maximize and do not affect the selected slope. Equal copies give the same slope. This gives precisely the original first-maximizing-index map.

Slopes that never receive positive rho-mass need not be removed. Give every retained slope its rank in the fixed order. Unused slopes have lambda-mass zero and hence zero second-marginal mass in every competing coupling; they cause no difficulty below.

### Proof

Relabel the ordered distinct slopes as y1,...,yN and write r(yi)=i. Their first-maximizer regions are Borel. The original slack and finite-cost argument apply with no regularity assumption on rho:

    s(x,y) = u(x)−x·y−c(y) ≥ 0.

All terms are integrable because there are finitely many slopes and rho has finite second moment. The graph plan has zero slack everywhere and is optimal.

If pi is another optimal plan, it also has zero slack almost everywhere. Therefore, for pi-almost every (x,y), y is a maximizing slope at x. As T(x) is the earliest maximizing slope,

    r(y) − r(T(x)) ≥ 0.

This integer-valued difference is bounded. The first marginal is rho and the second is lambda=T#rho, so

    integral r(y) d pi = sum_i i lambda({yi})
                       = integral r(T(x)) d rho
                       = integral r(T(x)) d pi.

The nonnegative difference has integral zero and vanishes pi-almost everywhere. Distinct ranks identify distinct slopes, giving y=T(x) almost everywhere. The plan is the graph plan, proving uniqueness.

The no-tie condition for the gradient assertion cannot simply be deleted. For rho=delta_0 and u(x)=|x| on R, the selected induced plan is unique, but u is not differentiable at the only source point.

Nor may “fixed total order” be replaced by arbitrary tie selection under a singular source. For example, let u(x1,x2)=|x1| and rho=(delta_(0,−1)+delta_(0,1))/2. Both slopes −e1,e1 maximize at both source points. A selection assigning a different slope to each point induces lambda=(delta_(−1,0)+delta_(1,0))/2. Every source-to-target pair has squared distance two, so multiple couplings are optimal. The fixed-priority hypothesis is what excludes this example for the induced law in the statement.

## What persists when all three atom masses are fixed

### Statement

Fix d≥2 and rho uniform on [−1,1]^d. For 0<b<1/4, use

    u(x)=max(−x1,x1,1/4),
    v_b(x)=max(−x1,x1,1/4+b x2).

Let mu and nu_b be the induced targets. Their atom masses are fixed at 3/8, 1/4, 3/8, and the distance between any two atoms within either target is at least one. Their unique quadratic optimal maps satisfy, for every finite p≥1,

    Wp(mu,nu_b) = 4^(−1/p)b,
    W-infinity(mu,nu_b) = b,
    ||T_mu−T_nu_b||_2² = b/2 + b²/4,
    ||T_mu−T_nu_b||_infinity = sqrt(1+b²).

Consequently no uniform L2 map estimate with exponent alpha>1/2 in any Wp, including W-infinity, can hold on even this fixed-mass three-atom class. The target-to-map assignment is also not continuous at this fixed mu when the targets use any of these Wasserstein metrics and the maps use the essential-supremum norm.

### Proof

Set a=1/4 in the already-verified two-parameter construction. The condition 0<b<1/4 implies 0<b<a and a+b<1. All displayed identities follow directly from its cell masses, projection lower bound, and map-distance formulas. The atom locations in mu are −e1,0,e1; in nu_b they are −e1,b e2,e1. Their minimum within-target separation is at least one.

For finite p, the L2-to-Wp^alpha ratio is

    4^(alpha/p) sqrt(1/2+b/4) b^(1/2−alpha).

It tends to infinity when alpha>1/2. For W-infinity the same expression holds without the factor 4^(alpha/p). Meanwhile nu_b converges to the fixed target mu in every Wp, including W-infinity, but the map essential-supremum difference tends to one. This proves both assertions.

### Scope

This fixed-mass family does not give the 1/3 W2 or 1/4 W1 obstruction established by the vanishing-mass family b=a/2. It leaves open, on a fixed positive-mass class, all positive upper-estimate questions not directly excluded by its 1/2 ceiling. In particular, the calculation does not prove a matching 1/2 upper bound. The reviewed proof's decision not to assert a fixed-mass conclusion is not an error; this is a separately stated consequence of its wider formulas.
