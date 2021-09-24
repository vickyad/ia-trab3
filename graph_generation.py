import plotly.graph_objects as go
import eight_queens as eq


def run_ga_with_data_generation(g, n, k, m, e):
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
    min_conflicts_per_generation = []
    max_conflicts_per_generation = []
    average_conflicts_per_generation = []
    current_population = eq.generate_population(n)

    for generation in range(g):
        conflicts = []
        for individual in current_population:
            conflicts.append(eq.evaluate(individual))
        min_conflicts_per_generation.append(min(conflicts))
        max_conflicts_per_generation.append(max(conflicts))
        average_conflicts_per_generation.append(sum(conflicts)/len(conflicts))

        new_population = []
        if e:
            new_population.append(eq.tournament(current_population))
        while len(new_population) < n:
            first_selection = eq.select_individuals(current_population[:], k)
            parent_1 = eq.tournament(first_selection)

            current_population.pop(current_population.index(parent_1))
            second_selection = eq.select_individuals(current_population[:], k)
            parent_2 = eq.tournament(second_selection)

            offspring_1, offspring_2 = eq.crossover(parent_1, parent_2, partitioner)
            offspring_1 = eq.mutate(offspring_1, m)
            offspring_2 = eq.mutate(offspring_2, m)
            new_population.extend([offspring_1, offspring_2])
        current_population = new_population
    generate_graph(min_conflicts_per_generation, max_conflicts_per_generation, average_conflicts_per_generation)
    return eq.tournament(current_population)


def generate_graph(min_values, max_values, average_values):
    y = [i for i in range(len(min_values))]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y, y=min_values, name="menor conflito", line_shape='linear'))
    fig.add_trace(go.Scatter(x=y, y=max_values, name="maior conflito", line_shape='linear'))
    fig.add_trace(go.Scatter(x=y, y=average_values, name="conflito médio", line_shape='linear'))

    fig.update_layout(title='Desempenho do algoritmo genético no problema das 8 rainhas',
                      xaxis_title='Geração',
                      yaxis_title='Conflitos')
    fig.show()
