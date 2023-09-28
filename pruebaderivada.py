from sympy import symbols, Eq, solve, log

# Definir las variables como símbolos
x, y = symbols('x y')

# Definir los valores específicos de a, b y c
a_val = 10
  # Sustituye con tu valor de a
b_val = 10  # Sustituye con tu valor de b
c_val = 100  # Sustituye con tu valor de c

# Definir la función objetivo
f = 0.7 * log(x) + log(y)

# Definir la restricción y sustituir los valores de a, b y c
restriccion = Eq(a_val*x + b_val*y, c_val)

# Resolver la restricción para y
y_sol = solve(restriccion, y)[0]

# Sustituir y en la función objetivo
f_sustituida = f.subs(y, y_sol)

# Derivar la función sustituida respecto a x y resolver
df_dx = f_sustituida.diff(x)
x_sol = solve(df_dx, x)[0]

# Sustituir el valor de x encontrado en la expresión de y
y_sol_sustituida = y_sol.subs(x, x_sol)

print("x =", x_sol.evalf())
print("y =", y_sol_sustituida.evalf())