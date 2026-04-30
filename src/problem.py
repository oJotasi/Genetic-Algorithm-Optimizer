import numpy as np

class BinaryLinearProblem:
    """
    Problema de optimización binaria:

    maximizar: c · x
    Sujeto a: A · x <= b
    x ∈ {0,1}
    """

    def __init__(self, A, b, c, penalty_weight=1000):
        self.A = np.array(A)
        self.b = np.array(b)
        self.c = np.array(c)
        self.penalty_weight = penalty_weight

    def fitness(self, x):
        x = np.array(x)
        Ax = self.A @ x

        # penalización por violaciones
        violaciones = Ax - self.b
        penalty = np.sum(violaciones[violaciones > 0]) * self.penalty_weight

        # maximización (convertido a minimización negativa)
        value = -(self.c @ x)

        return value - penalty

    def is_feasible(self, x):
        return np.all(self.A @ np.array(x) <= self.b)
