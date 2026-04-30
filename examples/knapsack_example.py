import numpy as np
from src.problem import BinaryLinearProblem
from src.ga import GeneticAlgorithm


A = np.array([
    [2, 3, 4, 0, 0],
    [0, 0, 3, 5, 6],
    [1, 1, 0, 1, 0]
])

b = np.array([7, 9, 2])
c = np.array([6, 5, 8, 7, 4])

problem = BinaryLinearProblem(A, b, c)

ga = GeneticAlgorithm(problem)

sol, fit = ga.run()

print("\n============================")
print("MEJOR SOLUCIÓN")
print("x =", sol)
print("Valor objetivo =", c @ np.array(sol))
print("Factible =", problem.is_feasible(sol))
print("============================")
