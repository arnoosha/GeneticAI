import random
import math
import time

def equation1(x, y, z, alpha):
    return alpha * x + y * x**2 + y**3 + z**3

def equation2(x, y, z, beta):
    return beta * y + math.sin(y) + 2**y - z + math.log10(abs(x) + 1)

def equation3(x, y, z, theta):
    return theta * z + y - (math.cos(x + y) / math.sin(z * y - y**2 + z) + 2)

def solver(alpha, beta, theta):


    start_time = time.time()
    population_size = 100
    mutation_rate = 0.1
    max_generations = 1000
    best_solution = None
    best_error = float('inf')

    def generate_population():
        return [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(population_size)]


    def squared_error(x, y, z, alpha, beta, theta):
        error1 = equation1(x, y, z, alpha)**2
        error2 = equation2(x, y, z, beta)**2
        error3 = equation3(x, y, z, theta)**2
        return error1 + error2 + error3

    def selection(population, scores):
       # return random.choices(population, weights=[1 / (s + 1) for s in scores], k=2)
        def selection(population, scores, tournament_size=3):
            selected = []
            for _ in range(tournament_size):
                i = random.randint(0, len(population) - 1)
                selected.append((population[i], scores[i]))
            return min(selected, key=lambda ind:

    def crossover(parent1, parent2):
        crossover_point = random.randint(1, 2)
        return parent1[:crossover_point] + parent2[crossover_point:]

    def mutation(child):
        if random.random() < mutation_rate:
            mutation_gene = random.randint(0, 2)
            child = list(child)
            child[mutation_gene] = random.uniform(-10, 10)
            return tuple(child)
        return child

    population = generate_population()

    while (time.time() - start_time) < 4:
        scores = [squared_error(x, y, z, alpha, beta, theta) for x, y, z in population]
        min_error = min(scores)
        min_index = scores.index(min_error)
        if min_error < best_error:
            best_error = min_error
            best_solution = population[min_index]

        if best_error <= 0.001:
            break

        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, scores)
            child = crossover(parent1, parent2)
            child = mutation(child)
            new_population.extend([parent1, parent2, child])

        population = new_population[:population_size]

    return best_solution

