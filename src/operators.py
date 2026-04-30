import random

def generar_individuo(n):
    return [random.randint(0, 1) for _ in range(n)]


def seleccion_ruleta(poblacion, fitnesses):
    min_f = min(fitnesses)
    shift = abs(min_f) + 1
    fitness_pos = [f + shift for f in fitnesses]

    idx = random.choices(range(len(poblacion)), weights=fitness_pos, k=2)
    return poblacion[idx[0]], poblacion[idx[1]]


def cruce_un_punto(p1, p2, tasa_cruce):
    if random.random() < tasa_cruce:
        punto = random.randint(1, len(p1) - 1)
        return p1[:punto] + p2[punto:]
    return p1[:]


def mutacion_bitflip(individuo, prob):
    return [(1 - bit) if random.random() < prob else bit for bit in individuo]
