# Genetic Algorithm Solver for Nonlinear Equation System

This project implements a **Genetic Algorithm (GA)** to find real-valued solutions \((x, y, z)\) that (approximately) satisfy a system of three nonlinear equations with tunable coefficients \(\alpha, \beta, \theta\).

The solver searches over continuous domains and minimizes the **sum of squared residuals** of the three equations within a strict wall-clock time budget.

---

## Problem Formulation

We seek \((x, y, z) \in \mathbb{R}^3\) such that:

\[
\begin{aligned}
f_1(x,y,z;\alpha) &= \alpha x + y x^2 + y^3 + z^3 = 0 \\
f_2(x,y,z;\beta)  &= \beta y + \sin(y) + 2^{\,y} - z + \log_{10}(|x| + 1) = 0 \\
f_3(x,y,z;\theta) &= \theta z + y - \Big(\frac{\cos(x+y)}{\sin(zy - y^2 + z)} + 2\Big) = 0
\end{aligned}
\]

**Objective (fitness to minimize):**
\[
E(x,y,z) \;=\; f_1^2 + f_2^2 + f_3^2
\]

A candidate solution with smaller \(E\) better satisfies the system.

---

## Method

The solver uses a **Genetic Algorithm** with the following components:

- **Representation**: An individual is a tuple \((x,y,z)\).
- **Initialization**: Random uniform sampling for each gene in \([-10, 10]\).
- **Fitness**: Sum of squared residuals \(E(x,y,z)\).
- **Selection**: Tournament (recommended) or fitness-proportional variants.
- **Crossover**: One-point crossover on the 3-gene chromosome.
- **Mutation**: With probability `mutation_rate`, replace one gene with a fresh uniform sample in \([-10, 10]\).
- **Replacement**: Generate offspring to form the next population.
- **Stopping**: 
  - 4 seconds wall-clock time (hard budget), or
  - \(E \le 10^{-3}\), or
  - Max generations reached.

---

## Key Parameters (defaults in code)

- `population_size = 100`  
- `mutation_rate = 0.1`  
- `max_generations = 1000`  
- **Search domain** for each gene: \([-10, 10]\)  
- **Time budget**: ~4 seconds per `solver` call

---
## Implementation Notes

- Fitness function:

  - equation1(x, y, z, alpha)

  - equation2(x, y, z, beta)

  - equation3(x, y, z, theta)


- Time-aware loop: The evolutionary loop stops when time.time() - start_time > 4.

- Dynamic difficulty: The landscape is highly nonconvex (sin, cos, power, division), so global optimality is not guaranteed. GA offers a robust anytime heuristic.
