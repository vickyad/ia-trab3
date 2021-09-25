def h_theta(x, theta_0, theta_1):
    return theta_0 + theta_1 * x


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    data_len = len(data)
    f_somatory = 0
    for i in range(data_len):
        f_somatory += (h_theta(data[i][0], theta_0, theta_1) - data[i][1]) ** 2
    return 1/data_len * f_somatory


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    data_len = len(data)
    theta_0_sum = 0
    theta_1_sum = 0
    for i in range(data_len):
        theta_0_sum += h_theta(data[i][0], theta_0, theta_1) - data[i][1]
        theta_1_sum += (h_theta(data[i][0], theta_0, theta_1) - data[i][1]) * data[i][0]
    theta_0 = theta_0 - alpha * (2/data_len * theta_0_sum)
    theta_1 = theta_1 - alpha * (2/data_len * theta_1_sum)
    return theta_0, theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    theta_0_list = [theta_0]
    theta_1_list = [theta_1]
    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        theta_0_list.append(theta_0)
        theta_1_list.append(theta_1)

    return theta_0_list, theta_1_list
