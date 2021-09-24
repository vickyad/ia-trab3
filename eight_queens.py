from random import random, randint

QUEENS_QUANTITY = 8


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    conflicts = 0
    for i in range(7):
        for j in range(i + 1, QUEENS_QUANTITY):
            if individual[i] == individual[j]:
                conflicts += 1
            elif i - individual[i] == j - individual[j] or i + individual[i] == j + individual[j]:
                conflicts += 1
    return conflicts


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    current_best = participants[0]
    for individual in participants:
        if evaluate(individual) < evaluate(current_best):
            current_best = individual
    return current_best


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    new_a1 = parent1[0:index] + parent2[index:]
    new_a2 = parent2[0:index] + parent1[index:]
    return new_a1, new_a2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random() < m:
        new_position = int(randint(0, QUEENS_QUANTITY - 1))
        new_value = int(randint(1, QUEENS_QUANTITY))
        individual[new_position] = new_value
    return individual


def generate_population(size):
    return [generate_random_individual() for i in range(size)]


def generate_random_individual():
    return [randint(1, QUEENS_QUANTITY) for i in range(QUEENS_QUANTITY)]


def select_individuals(individual_list, selection_size):
    selected_list = []
    original_list_size = len(individual_list)
    for i in range(selection_size):
        if original_list_size > 1:
            selected_value = individual_list.pop(randint(0, original_list_size - 1))
        else:
            selected_value = individual_list[0]
        selected_list.append(selected_value)
        original_list_size -= 1
    return selected_list


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    partitioner = 4
    current_population = generate_population(n)
    conflicts = []
    for individual in current_population:
        conflicts.append(evaluate(individual))

    for generation in range(g):
        new_population = []
        if e:
            new_population.append(tournament(current_population))
        while len(new_population) < n:
            first_selection = select_individuals(current_population[:], k)
            parent_1 = tournament(first_selection)

            current_population.pop(current_population.index(parent_1))
            second_selection = select_individuals(current_population[:], k)
            parent_2 = tournament(second_selection)

            offspring_1, offspring_2 = crossover(parent_1, parent_2, partitioner)
            offspring_1 = mutate(offspring_1, m)
            offspring_2 = mutate(offspring_2, m)
            new_population.extend([offspring_1, offspring_2])
        current_population = new_population
    return tournament(current_population)