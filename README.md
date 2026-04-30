# Genetic-Algorithm-Optimizer
Optimización combinatoria con restricciones usando Algoritmos Genéticos

Este proyecto implementa un **Algoritmo Genético (GA)** para resolver problemas de **optimización combinatoria binaria con restricciones lineales**, del tipo:

### Formulación del problema

Maximizar:

    c · x

Sujeto a:

    A · x ≤ b  
    x ∈ {0,1}

---

## Características principales

- Representación binaria de soluciones (cromosomas)
- Manejo de restricciones mediante **funciones de penalización**
- Estrategia de **elitismo** (conservación del mejor individuo)
- **Mutación adaptativa** para mejorar la exploración
- Detección de **estancamiento** (convergencia prematura)
- **Reinicio parcial de la población** para escapar de óptimos locales

---

## Enfoque y técnicas utilizadas

- Algoritmos evolutivos
- Optimización combinatoria
- Penalización de restricciones (Constraint Handling)
- Balance entre **exploración vs explotación**

---
## Como ejecutar

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/genetic-algorithm-optimizer.git
cd genetic-algorithm-optimizer
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar un ejemplo

```bash
python -m examples.knapsack_example
```

---

## Autor

José Andrade
