from sympy import symbols, diff, exp, ln
import math 
# Definir símbolos
F = 300
P = 100
n = symbols('n')

# Definir la función k
k = exp(ln(F/P)/n) - 1

# Calcular la derivada dk/dn
derivada = diff(k, n)

# Imprimir la derivada


print(derivada)


