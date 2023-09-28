import numpy as np
from scipy.optimize import minimize

# Define los coeficientes a, b y c
a = 1  # Puedes cambiarlo por el valor que desees
b = 1  # Puedes cambiarlo por el valor que desees
c = 1  # Puedes cambiarlo por el valor que desees

# Define la función objetivo
def objective_function(vars):
    x, y = vars
    return a * x + b * y

# Define la restricción
def constraint_function(vars):
    x, y = vars
    return 0.7 * np.log(x) + np.log(y) - c

# Define el tipo de restricción
constraint = {'type': 'eq', 'fun': constraint_function}

# Define un punto de partida para la optimización
initial_guess = [1, 1]  # Puedes cambiarlo por el valor que desees

# Realiza la optimización
result = minimize(objective_function, initial_guess, constraints=constraint, method='SLSQP')

# Imprime los resultados
if result.success:
    optimized_x, optimized_y = result.x
    print(f'Optimized x: {optimized_x}')
    print(f'Optimized y: {optimized_y}')
    print(f'Minimum value of the objective function: {result.fun}')
else:
    print('Optimization failed:', result.message)