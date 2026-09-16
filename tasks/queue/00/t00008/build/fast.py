"""Fast exact integer linear algebra: Bareiss determinant and Smith normal form."""
def det_bareiss(M):
    M=[r[:] for r in M]; n=len(M); sign=1; prev=1
    for k in range(n-1):
        if M[k][k]==0:
            for i in range(k+1,n):
                if M[i][k]!=0: M[k],M[i]=M[i],M[k]; sign=-sign; break
            else: return 0
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
        prev=M[k][k]
    return sign*M[n-1][n-1]

def smith(M):
    """Invariant factors of an integer matrix, by classical reduction."""
    A=[r[:] for r in M]; n=len(A); m=len(A[0]); res=[]; r=c=0
    def swap_rows(i,j): A[i],A[j]=A[j],A[i]
    def swap_cols(i,j):
        for row in A: row[i],row[j]=row[j],row[i]
    while r<n and c<m:
        piv=None; bestv=None
        for i in range(r,n):
            for j in range(c,m):
                if A[i][j]!=0 and (bestv is None or abs(A[i][j])<bestv):
                    bestv=abs(A[i][j]); piv=(i,j)
        if piv is None: break
        swap_rows(r,piv[0]); swap_cols(c,piv[1])
        while True:
            done=True
            for i in range(r+1,n):
                if A[i][c]%A[r][c]:
                    q=A[i][c]//A[r][c]
                    for j in range(c,m): A[i][j]-=q*A[r][j]
                    swap_rows(r,i); done=False
            for i in range(r+1,n):
                if A[i][c]:
                    q=A[i][c]//A[r][c]
                    for j in range(c,m): A[i][j]-=q*A[r][j]
            for j in range(c+1,m):
                if A[r][j]%A[r][c]:
                    q=A[r][j]//A[r][c]
                    for i in range(r,n): A[i][j]-=q*A[i][c]
                    swap_cols(c,j); done=False
            for j in range(c+1,m):
                if A[r][j]:
                    q=A[r][j]//A[r][c]
                    for i in range(r,n): A[i][j]-=q*A[i][c]
            if done and all(A[i][c]==0 for i in range(r+1,n)) and all(A[r][j]==0 for j in range(c+1,m)):
                break
        res.append(abs(A[r][c])); r+=1; c+=1
    # enforce the divisibility chain
    changed=True
    while changed:
        changed=False
        for i in range(len(res)-1):
            a,b=res[i],res[i+1]
            if b % a:
                from math import gcd
                g=gcd(a,b); l=a*b//g
                res[i],res[i+1]=g,l; changed=True
    return res
