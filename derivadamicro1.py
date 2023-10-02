from sympy import symbols, Eq, solve, log
import math
import numpy as np

# Definir las variables como símbolos
x, y = symbols('x y')

# Definir los coeficientes como símbolos
a, b, c = symbols('a b c')

# Definir la función objetivo
f = 0.7 * log(x) + log(y)

# Definir la restricción
a = 10
b = 10
c= 100
restriccion = Eq(a*x + b*y, c)

# Resolver la restricción para y
y_sol = solve(restriccion, y)[0]

# Sustituir y en la función objetivo
f_sustituida = f.subs(y, y_sol)

# Derivar la función sustituida respecto a x y resolver
df_dx = f_sustituida.diff(x)
x_sol = solve(df_dx, x)[0]

# Sustituir el valor de x encontrado en la expresión de y
y_sol_sustituida = y_sol.subs(x, x_sol)

print("x =", x_sol)
print("y =", y_sol_sustituida)

# hallar x teniendo en cuenta la restricción
x = np.linspace(0, 100, 100)
y = (c - a*x)/b


