import random
from individual import Individual
from functions import slice_sequence, score_population, select_mates
import copy

# Huge sentence.
with open("sentence.txt") as f:
    sequence = f.readlines()

sequence = [x.replace(" ", "").lower().strip() for x in sequence]
sequence = "".join(sequence)


# Dictionary of words.
with open("dictionary.txt") as d:
    dictionary = d.readlines()

dictionary = [x.strip() for x in dictionary] 

#example =  "thisisasentencethatwillbejoined"
# Solution: 000101100000001000100010100000000000

POPULATION_SIZE = 100
INDIVIDUAL_LENGTH = len(sequence) - 1
NUMBER_GENERATIONS = 1000
EVOLUTION_STOP = 200

population = []
# Generates initial random population!
for i in xrange(POPULATION_SIZE):
    genes = bin(random.getrandbits(INDIVIDUAL_LENGTH))[2:INDIVIDUAL_LENGTH+2]
    individual = Individual('0'*(INDIVIDUAL_LENGTH - len(genes)) + genes)
    population.append(individual)

# Partitions the letter sequence, according to individual genes.
stuck = 0
elitist = population[0]
for i in xrange(NUMBER_GENERATIONS):
    population = slice_sequence(population, sequence)
    population = score_population(population, dictionary)
    print("%d: %s - %d errors (%d)" % (i+1 ,population[-1], population[-1].errors, stuck))
    
    # Exit conditions. 
    # First by perfect match.
    if population[-1].errors == 0:
        break

    # Then by stuck evolution.
    if population[-1].errors == elitist.errors/2:
        stuck += 1
        if stuck > EVOLUTION_STOP:
            break
    else:
        stuck = 0

    elitist = population[-1].copy() # Best individual.

    # Selection
    mating_pairs = select_mates(population)

    # Crossover
    population = []
    for mates in mating_pairs:
        first = mates[0]
        second = mates[1]

        children = first.crossover(second)
        population.append(children[0])
        population.append(children[1])

    # Mutation
    for k,individual in enumerate(population):
        population[k].gene = individual.mutate()

    # Elitism
    population.sort(key=lambda x: x.errors, reverse=True)
    population[0] = elitist

print("\nBest individual - %s" % population[-1].genes)