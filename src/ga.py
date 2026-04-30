import random
import numpy as np
from .operators import generar_individuo, seleccion_ruleta, cruce_un_punto, mutacion_bitflip


class GeneticAlgorithm:
    def __init__(
        self,
        problem,
        num_individuos=50,
        max_generaciones=100,
        tasa_cruce=0.8,
        tasa_mutacion=0.1,
        limite_estancamiento=20,
        seed=42
    ):
        self.problem = problem
        self.num_individuos = num_individuos
        self.max_generaciones = max_generaciones
        self.tasa_cruce = tasa_cruce
        self.tasa_mutacion = tasa_mutacion
        self.limite_estancamiento = limite_estancamiento

        random.seed(seed)
        np.random.seed(seed)

    def run(self, verbose=True):
        n = len(self.problem.c)

        poblacion = [generar_individuo(n) for _ in range(self.num_individuos)]

        mejor_global = None
        mejor_fitness = float("-inf")

        generaciones_sin_mejora = 0
        mutacion_actual = self.tasa_mutacion
        modo_recuperacion = False

        for gen in range(self.max_generaciones):

            fitnesses = [self.problem.fitness(ind) for ind in poblacion]
            idx_best = np.argmax(fitnesses)

            if fitnesses[idx_best] > mejor_fitness:
                mejor_fitness = fitnesses[idx_best]
                mejor_global = poblacion[idx_best]
                generaciones_sin_mejora = 0
                mutacion_actual = self.tasa_mutacion
                modo_recuperacion = False
            else:
                generaciones_sin_mejora += 1

            # Estancamiento
            if generaciones_sin_mejora >= self.limite_estancamiento:
                if verbose:
                    print(f"[INFO] Estancamiento en generación {gen}")

                if modo_recuperacion:
                    if verbose:
                        print("[FIN] Sin mejora tras recuperación")
                    break

                mitad = self.num_individuos // 2
                for i in range(mitad, self.num_individuos):
                    poblacion[i] = generar_individuo(n)

                mutacion_actual = 0.4
                generaciones_sin_mejora = 0
                modo_recuperacion = True

            # Nueva población (elitismo)
            nueva = [mejor_global]

            while len(nueva) < self.num_individuos:
                p1, p2 = seleccion_ruleta(poblacion, fitnesses)
                hijo = cruce_un_punto(p1, p2, self.tasa_cruce)
                hijo = mutacion_bitflip(hijo, mutacion_actual)
                nueva.append(hijo)

            poblacion = nueva

            if verbose and gen % 10 == 0:
                print(f"Gen {gen}: mejor fitness = {mejor_fitness}")

        return mejor_global, mejor_fitness
