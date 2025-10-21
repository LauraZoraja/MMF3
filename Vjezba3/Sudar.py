import math

# parametri
y01, A, B = 5.0, 1.0, 3.0
y02, C, D = 0.325, 2.0, 0.5

def f1(t):
    return y01 + A*math.cos(B*t)

def f2(t):
    return y02 + C*math.exp(D*t)

def df1(t):
    return -A*B*math.sin(B*t)

def df2(t):
    return C*D*math.exp(D*t)

def f(t):
    return f1(t) - f2(t)

def df(t):
    return df1(t) - df2(t)

# Bisection
def bisekcija(a, b, tol=10**(-6), Nmax=200):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("preduvjeti nisu zadovoljeni: f(a) i f(b) moraju imati suprotne znakove")
    for i in range(1, Nmax+1):
        c = 0.5 * (a + b)
        fc = f(c)
        print("{:2d} {:.10f}".format(i, c))  # print iteration number and c as in the PDF
        if abs(fc) < tol or (b - a)*0.5 < tol:
            return c, i
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return 0.5*(a+b), Nmax

# Newton-Raphson
def newton(x0, tol=10**(-10), Nmax=100):
    x = x0
    for i in range(1, Nmax + 1):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 10**(-16):
            raise ValueError("Derivacija premala")
        xnew = x - fx/dfx
        if abs(xnew - x) < tol:
            return xnew, i
        x = xnew
    return x, Nmax

# izvršavanje
t_bis, iter_bis = bisekcija(2.0, 2.2, tol=1e-12)
t_newt, iter_newt = newton(2.1, tol=1e-12)

y_at_t_bis = y01 + A*math.cos(B*t_bis)
y_at_t_newt = y01 + A*math.cos(B*t_newt)

diff_bis = abs(f1(t_bis) - f2(t_bis))
diff_newt = abs(f1(t_newt) - f2(t_newt))

print("Bisekcija: t = {:.12f}, iteracije = {}, y = {:.12f}".format(t_bis, iter_bis, diff_bis))
print("Newton:    t = {:.12f}, iteracije = {}, y = {:.12f}".format(t_newt, iter_newt, diff_newt))
