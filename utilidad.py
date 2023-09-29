import numpy as np
import sympy as sp
from sympy import symbols, simplify

# Define las variables
x, y, z = symbols('x y z')

# Define la expresión algebraica
expresion = (x + x*y + x*y*z) / x

# Simplifica la expresión
expresion_simplificada = simplify(expresion)

# Imprime la expresión original y la simplificada
print(f"Expresión Original: {expresion}")
print(f"Expresión Simplificada: {expresion_simplificada}")