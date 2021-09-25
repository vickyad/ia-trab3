import unittest
import eight_queens


class TestEightQueens(unittest.TestCase):
    def test_evaluate(self):
        """
        Teste basico com o exemplo do enunciado
        :return:
        """
        self.assertEqual(8, eight_queens.evaluate([2, 2, 4, 8, 1, 6, 3, 4]))

    def test_tournament(self):
        """
        Teste simples com dois individuos parecidos
        :return:
        """
        participants = [
            [2, 2, 4, 8, 1, 6, 3, 4],  # 8 conflitos
            [2, 7, 4, 8, 1, 6, 3, 4],  # 7 conflitos
        ]

        self.assertEqual([2, 7, 4, 8, 1, 6, 3, 4], eight_queens.tournament(participants))

    def test_crossover(self):
        """
        Teste com o exemplo do enunciado
        :return:
        """
        parent1 = [2, 4, 7, 4, 8, 5, 5, 2]
        parent2 = [3, 2, 7, 5, 2, 4, 1, 1]

        offspring1, offspring2 = eight_queens.crossover(parent1, parent2, 3)

        children = [offspring1, offspring2]

        self.assertIn([2, 4, 7, 5, 2, 4, 1, 1], children)
        self.assertIn([3, 2, 7, 4, 8, 5, 5, 2], children)

    def test_mutate_prob_zero(self):
        """
        Teste simples: mutacao com prob = 0 deve retornar o individuo intacto
        :return:
        """
        original = [2, 4, 7, 4, 8, 5, 5, 2]
        mutated = eight_queens.mutate(original, 0)
        self.assertEqual(original, mutated)

    def test_mutate_prob_one(self):
        """
        Teste simples: mutacao com prob = 1 deve retornar um individuo diferente.
        Porem, pode haver o 'azar' da mutacao sortear o mesmo numero que ja estava.
        Assim, se esse teste falhar, rode-o novamente para verificar se a falha foi
        devido ao azar ou se o codigo esta mesmo com problema.
        :return:
        """
        original = [2, 4, 7, 4, 8, 5, 5, 2]
        mutated = eight_queens.mutate(original, 1)
        self.assertNotEqual(original, mutated)


if __name__ == '__main__':
    unittest.main()
