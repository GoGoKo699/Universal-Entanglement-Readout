"""Exact rational checks for the full-rank qubit-qutrit corner."""
from fractions import Fraction as Q
import json
N=6
def pt(a):
    return [[a[(c//3)*3+r%3][(r//3)*3+c%3] for c in range(N)] for r in range(N)]
def det(a):
    a=[[Q(x) for x in row] for row in a]; n=len(a); out=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None: return Q(0)
        if pivot!=j: a[pivot],a[j]=a[j],a[pivot]; out=-out
        p=a[j][j]; out*=p
        for i in range(j+1,n):
            q=a[i][j]/p
            for k in range(j+1,n): a[i][k]-=q*a[j][k]
    return out
def matvec(a,v):
    return [sum(a[i][j]*v[j] for j in range(len(v))) for i in range(len(a))]
def scale(a,q):
    return [[q*x for x in row] for row in a]
def add(*args):
    return [[sum(a[i][j] for a in args) for j in range(N)] for i in range(N)]

def check():
    # Product vectors are built with Gaussian integers, without floating point.
    def gmul(a,b):
        return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    def conjugate(a):
        return (a[0],-a[1])
    def outer_sum(vectors):
        a=[[(0,0) for _ in range(N)] for _ in range(N)]
        for vector in vectors:
            for i in range(N):
                for j in range(N):
                    z=gmul(vector[i],conjugate(vector[j]))
                    a[i][j]=(a[i][j][0]+z[0],a[i][j][1]+z[1])
        assert all(z[1]==0 for row in a for z in row)
        return [[Q(z[0]) for z in row] for row in a]
    vectors_r=[]; vectors_x=[]
    for z in [(0,0),(1,0),(-1,0),(0,1),(0,-1),(2,0)]:
        b=[(1,0),z,gmul(z,z)]
        vectors_r.append([gmul(a,c) for a in [(1,0),conjugate(z)] for c in b])
        vectors_x.append([gmul(a,c) for a in [(1,0),z] for c in b])
    R=outer_sum(vectors_r); X=outer_sum(vectors_x)
    u=[0,1,0,-1,0,0]; v=[0,0,1,0,-1,0]
    Pu=[[Q(u[i]*u[j],2) for j in range(N)] for i in range(N)]
    Pv=[[Q(v[i]*v[j],2) for j in range(N)] for i in range(N)]
    assert sum(R[i][i] for i in range(N))==130 and pt(R)==X
    assert matvec(X,u)==[0]*N and matvec(X,v)==[0]*N
    assert sum(u[i]*v[i] for i in range(N))==0
    four=[0,1,2,5]
    assert det([[X[i][j] for j in four] for i in four])>0
    minors=[det([row[:k] for row in R[:k]]) for k in range(1,7)]
    assert minors==[6,44,496,2304,5120,9216]
    delta=Q(1,10000); rho0=scale(R,Q(1,130)); corners=[]
    for a in [-delta,delta]:
        for b in [-delta,delta]:
            rho=add(scale(rho0,1-a-b),scale(pt(Pu),a),scale(pt(Pv),b))
            assert all(rho[i][j]==rho[j][i] for i in range(N) for j in range(N))
            assert sum(rho[i][i] for i in range(N))==1
            principal=[det([row[:k] for row in rho[:k]]) for k in range(1,7)]
            assert all(x>0 for x in principal)
            assert pt(rho)==add(scale(X,Q(1-a-b,130)),scale(Pu,a),scale(Pv,b))
            assert matvec(pt(rho),u)==[a*x for x in u]
            assert matvec(pt(rho),v)==[b*x for x in v]
            corners.append({"s":str(a),"t":str(b),"all_leading_principal_minors_positive":True})
    result={
     "R":[[int(x) for x in row] for row in R],
     "trace_R":130,"principal_minors_R":[int(x) for x in minors],
     "rank_partial_transpose_R":4,"physical_square_delta":str(delta),
     "corners":corners,
     "full_square_positivity":"Convex combinations of the four positive-definite corners cover the entire square.",
     "PT_eigenvalue_structure":"s, t, and four positive eigenvalues (1-s-t)*eig_positive(X)/130.",
     "classification":"PPT iff s>=0 and t>=0 throughout the square. In 2x3 the PPT criterion is equivalent to separability.",
     "algebraic_identities_checked":True,
     "method":"Rational elimination and exact matrix identities; no numerical tolerance."
    }
    result["all_checks_passed"] = True
    return result

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
