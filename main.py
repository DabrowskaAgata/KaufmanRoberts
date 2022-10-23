def calc_x(M, V, a, t):
    X = [1] * (V+1)
    for n in range(1, V+1):
        summ = 0
        for i in range(0, M):
            if n >= t[i]:
                summ += a[i] * t[i] * X[n-t[i]]
        X[n] = summ/n
    return X

def calc_p0(X):
    s = 0
    for i in X:
        s += i
    return 1/s

def calc_pn(X, M, V, a, t):
    P = [1] * (V + 1)
    P[0] = calc_p0(X)
    for n in range(1, V+1):
        summ = 0
        for i in range(0, M):
            if n >= t[i]:
                summ += a[i] * t[i] * P[n - t[i]]
        P[n] = summ/n
    return P
    
def calc_bn(P, V, t, i = 1):
    summ = 0
    for n in range(V - t[i-1] + 1, V + 1):
        summ += P[n]
    return summ

def calc_all(M, V, t, a):
    X = calc_x(M, V, a, t)
    P = calc_pn(X, M, V, a, t)
    b = [1]*M
    i=0
    
    while i < M:
        b[i] = calc_bn(P, V, t, i+1)
        i +=1
        
    print("x= ", X)
    print("P= ", P)
    
    inc = 0
    while inc < M:
        print("b" + str(inc + 1), " = ", b[inc])
        inc += 1

M = 2
V = 3
a = [[0.4, 1], [3, 5]]
t = [[1, 2], [3, 4]]    
for ai in a:
    for ti in t:
        print("M= ", M)
        print("V= ", V)
        print("ai= ", ai)
        print("ti= ", ti)
        calc_all(M, V, ti, ai)
        print("\n")


