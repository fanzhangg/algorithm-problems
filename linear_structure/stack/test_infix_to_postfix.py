from unittest import TestCase

from infix_expression import *


class TestInfixToPostfix(TestCase):
    def test_plus_minus(self):
        self.assertEqual("1 2 +", infix_to_postfix("1 + 2"))
        self.assertEqual("1 2 + 3 +", infix_to_postfix("1 + 2 + 3"))
        self.assertEqual("1 2 + 3 + 4 +", infix_to_postfix("1 + 2 + 3 + 4"))
        self.assertEqual("1 2 -", infix_to_postfix("1 - 2"))
        self.assertEqual("1 2 - 3 +", infix_to_postfix("1 - 2 + 3"))
        self.assertEqual("1 2 - 3 + 4 -", infix_to_postfix("1 - 2 + 3 - 4"))

    def test_times_divide(self):
        self.assertEqual("1 2 * 3 *", infix_to_postfix("1 * 2 * 3"))

    def test_power(self):
        self.assertEqual("5 3 4 2 - ** *", infix_to_postfix("5 * 3 ** ( 4 - 2 )"))

    def test_operators_with_diff_precedence(self):
        self.assertEqual("1 2 3 * +", infix_to_postfix("1 + 2 * 3"))
        self.assertEqual("1 2 3 * + 4 +", infix_to_postfix("1 + 2 * 3 + 4"))
        self.assertEqual("1 2 * 3 4 * +", infix_to_postfix("1 * 2 + 3 * 4"))

    def test_expression_with_parenthesis(self):
        self.assertEqual("1 2 + 3 *", infix_to_postfix("( 1 + 2 ) * 3"))
        self.assertEqual("1 2 + 3 4 + *", infix_to_postfix("( 1 + 2 ) * ( 3 + 4 )"))

    def test_has_higher_precedence(self):
        self.assertTrue(ge_precedence("*", "+"))
        self.assertFalse(ge_precedence("+", "*"))
        self.assertTrue(ge_precedence("+", "-"))


class TestCalc(TestCase):
    def test_valid_case(self):
        self.assertEqual(calc(1, "+", 2), 3)
        self.assertEqual(calc(1, "*", 2), 2)
        self.assertEqual(calc(1, "-", 2), -1)
        self.assertEqual(calc(1, "/", 2), 0.5)

    def test_invalid_operator(self):
        with self.assertRaises(SyntaxError):
            calc(1, "$", 2)


class TestEvalPostfix(TestCase):
    def test_valid_case(self):
        self.assertEqual(1 + 2, eval_postfix("1 2 +"))
        self.assertEqual(1 + 2 * 3, eval_postfix("1 2 3 * +"))
        self.assertEqual((1 + 2) * 3, eval_postfix("1 2 + 3 *"))
        self.assertEqual(9, eval_postfix("17 10 + 3 * 9 /"))

    def test_power(self):
        self.assertEqual(5 * 3 ** (4 - 2), eval_postfix("5 3 4 2 - ** *"))

    def test_invalid_operand(self):
        with self.assertRaises(SyntaxError):
            eval_postfix("a b +")


class TestInfixStrToList(TestCase):
    def test_int(self):
        self.assertEqual(["1", "+", "2", "-", "3", "*", "4", "/", "5"],
                         infix_str_to_list("1+2-3*4/5"))

    def test_decimal(self):
        self.assertEqual(["3.1415", "*", "2.734"], infix_str_to_list("3.1415*2.734"))

    def test_parenthesis(self):
        self.assertEqual(["(", "2", "+", "13", ")", "/", "2"], infix_str_to_list("(2+13)/2"))

    def test_power(self):
        self.assertEqual(["3", "**", "2", "+", "6"], infix_str_to_list("3**2+6"))

    def test_power_parenthesis(self):
        self.assertEqual(["(", "3", "+", "2", ")", "**", "(", "4", "+", "5", ")"], infix_str_to_list("(3+2)**(4+5)"))

    def test_invalid_case(self):
        with self.assertRaises(SyntaxError):
            infix_str_to_list("A+B+C")
        with self.assertRaises(SyntaxError):
            infix_str_to_list("1@2&3")
