f = int(input())
r = [list(map(int, input().split())) for i in range(f)]

def determinant(n, l):
    if n == 1:
        return l[0][0]
    elif n == 2:
        return l[0][0]*l[1][1]-l[1][0]*l[0][1]
    else:
        s = 0
        for i in range(n):
            minor = []
            for k in range(n):
                r = []
                for j in range(n):
                    if k != 0 and j != i:
                        r+=[l[k][j]]
                if r != []:
                    minor += [r]
            s += l[0][i]*determinant(n-1, minor)*(-1)**i
        return s

print(determinant(f, r))