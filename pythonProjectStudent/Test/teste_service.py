import unittest

from Domain.student_validator import StudentValidator
from Repository.student_repository import StudentRepository
from Service.student_service import StudentService


class TesteService(unittest.TestCase):
    def setUp(self):
        self.validator = StudentValidator()
        self.repository = StudentRepository()
        self.service = StudentService(self.repository, self.validator)

    def test_adauga_student(self):
        self.service.adauga(1, "Pop", "Maria", 345)
        studenti = self.service.get_all()
        self.assertEqual(len(studenti), 1)
        self.assertEqual(studenti[0].get_nume(), "Pop")
        self.assertEqual(studenti[0].get_prenume(), "Maria")
        self.assertEqual(studenti[0].get_grupa(), 345)
        with self.assertRaises(ValueError) as context:
            self.service.adauga(1, "ion", "vasile", 99)  # Nume și grup invalid
        self.assertIn("Numele trebuie sa inceapa cu litera mare si nu poate sa contina caractere speciale", str(context.exception))
        self.assertIn("Nr de grupa nu poate contine mai putin de 3 cifre", str(context.exception))

    def test_sterge_student(self):
        self.service.adauga(1, "Pop", "Maria", 345)
        self.service.sterge(1)
        studenti = self.service.get_all()
        self.assertEqual(len(studenti), 0)

    def test_modifica_student(self):
        self.service.adauga(1, "Pop", "Maria", 234)
        self.service.modifica(1, "Popa", "Ana", 354)
        studenti = self.service.get_all()
        self.assertEqual(studenti[0].get_nume(), "Popa")
        self.assertEqual(studenti[0].get_prenume(), "Ana")
        self.assertEqual(studenti[0].get_grupa(), 354)


if __name__ == "__main__":
    unittest.main()
