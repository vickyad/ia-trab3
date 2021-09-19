import unittest
import alegrete
import numpy as np


class TestAlegrete(unittest.TestCase):

    def test_compute_mse(self):
        data = np.genfromtxt('alegrete.csv', delimiter=',')
        mse = alegrete.compute_mse(0, 0, data)
        self.assertAlmostEqual(64.145467754, mse, 9)  # comparacao de floats com 9 casas de precisao

    def test_step_gradient(self):
        # dataset do Quiz de Otimizacao Continua
        data = np.array([
            [1, 3],
            [2, 4],
            [3, 4],
            [4, 2]
        ])

        new_theta0, new_theta1 = alegrete.step_gradient(1, 1, data, alpha=0.1)
        # comparacao de floats com precisao de 11 casas
        self.assertAlmostEqual(0.95, new_theta0, 11)
        self.assertAlmostEqual(0.55, new_theta1, 11)


if __name__ == '__main__':
    unittest.main()
