import unittest
import balanced_brackets


class TestBalancedBrackets(unittest.TestCase):

    def test_case_0(self):
        tests = [
            '{[()]}',
            '{[(])}',
            '{{[[(())]]}}'
        ]

        answers = [
            'YES',
            'NO',
            'YES'
        ]

        results = []

        for test in tests:
            results.append(balanced_brackets.isBalanced(test))

        self.assertEqual(results, answers)

    def test_case_1(self):
        tests = [
            '{{([])}}',
            '{{)[](}}'
        ]

        answers = [
            'YES',
            'NO'
        ]

        results = []

        for test in tests:
            results.append(balanced_brackets.isBalanced(test))

        self.assertEqual(results, answers)

    def test_case_2(self):
        tests = [
            '{(([])[])[]}',
            '{(([])[])[]]}',
            '{(([])[])[]}[]'
        ]

        answers = [
            'YES',
            'NO',
            'YES'
        ]

        results = []

        for test in tests:
            results.append(balanced_brackets.isBalanced(test))

        self.assertEqual(results, answers)


if __name__ == '__main__':
    unittest.main()