import unittest

from Domain.student import Student
from Domain.student_validator import StudentValidator


class TesteDomain(unittest.TestCase):
    def setUp(self):
        self.validator = StudentValidator()

    def test_student_valid(self):
        student = Student(2, "Pop", "Maria", 345)
        self.validator.valideaza(student)

    def test_nume_student_invalid(self):
        student = Student(3, "pop", "Maria", 456)
        with self.assertRaises(ValueError) as context:
            self.validator.valideaza(student)
        self.assertIn("Numele trebuie sa inceapa cu litera mare", str(context.exception))

    def test_grupa_student_invalida(self):
        student = Student(4, "Pop", "Maria", 2)
        with self.assertRaises(ValueError) as context:
            self.validator.valideaza(student)
        self.assertIn("Nr de grupa nu poate contine mai putin de 3 cifre", str(context.exception))
if __name__ == "__main__":
    unittest.main()
