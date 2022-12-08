from sympy import \*

x = Symbol('x', real = True)

y = ((-12*x)\*\*4)*(sin(cos(x)))-((18*x)\*\*3)+((5*x)\**2)+(10*x)-30

plot(y)

<sympy.plotting.plot.Plot at 0x7f537b28f0d0>

solve(y, x)

y.is_positive

y.is_nonnegative

Interval(-oo, oo).intersect(Interval(y,x))

[20736𝑥4sin(cos(𝑥))−5832𝑥3+25𝑥2+10𝑥−30,𝑥]
