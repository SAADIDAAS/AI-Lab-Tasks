import random

population_size = 6
number_of_generations = 15
mutation_rate = 0.1


def fitness_function(x):
    return x*x + 2*x


def decode_chromosome(binary_string):
    return int(binary_string, 2)


def create_random_chromosome():

    chromosome = ""

    for i in range(5):
        chromosome += random.choice("01")

    return chromosome


def select_parents(population_list):

    sorted_population = sorted(
        population_list,
        key=lambda chromosome: fitness_function(decode_chromosome(chromosome)),
        reverse=True
    )

    return sorted_population[:population_size // 2]


def perform_crossover(parent_one, parent_two):

    crossover_point = random.randint(1, 4)

    child = parent_one[:crossover_point] + parent_two[crossover_point:]

    return child


def perform_mutation(chromosome):

    chromosome_list = list(chromosome)

    mutation_index = random.randint(0, 4)

    if chromosome_list[mutation_index] == '0':
        chromosome_list[mutation_index] = '1'
    else:
        chromosome_list[mutation_index] = '0'

    return "".join(chromosome_list)


def genetic_algorithm():

    population = []

    for i in range(population_size):
        population.append(create_random_chromosome())

    for generation in range(number_of_generations):

        parents = select_parents(population)

        new_population = []

        while len(new_population) < population_size:

            parent_one, parent_two = random.sample(parents, 2)

            child = perform_crossover(parent_one, parent_two)

            if random.random() < mutation_rate:
                child = perform_mutation(child)

            new_population.append(child)

        population = new_population

    best_chromosome = max(
        population,
        key=lambda chromosome: fitness_function(decode_chromosome(chromosome))
    )

    best_x = decode_chromosome(best_chromosome)
    best_fitness = fitness_function(best_x)

    print("best chromosome:", best_chromosome)
    print("best value of x:", best_x)
    print("best fitness value:", best_fitness)


genetic_algorithm()
