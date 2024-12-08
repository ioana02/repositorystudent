import unittest

from Domain.student import Student
from Repository.student_repository import StudentRepository


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = StudentRepository()

    def test_adauga_student(self):
        student = Student(1, "Pop", "Maria", 243)
        self.repository.adauga(student)
        studenti = self.repository.get_all()
        self.assertEqual(len(studenti), 1)
        self.assertEqual(studenti[0].get_nume(), "Pop")
        self.assertEqual(studenti[0].get_prenume(), "Maria")
        self.assertEqual(studenti[0].get_grupa(), 243)
        student2 = Student(1, "Pop", "Maria", 243)
        try:
            self.repository.adauga(student2)
            if student.get_id() == student2.get_id() and student.get_nume() == student2.get_nume() and student.get_prenume() == student2.get_prenume() and student.get_grupa() == student2.get_grupa():
                print("Acest student a fost adăugat deja")
        except ValueError:
            "acest student a fost adaugat deja"

    def test_sterge_student(self):
        student = Student(1, "Pop", "Maria", 243)
        self.repository.adauga(student)
        self.repository.sterge(1)
        studenti = self.repository.get_all()
        self.assertEqual(len(studenti), 0)

    def test_get_student_dupa_id(self):
        student = Student(1, "Pop", "Maria", 234)
        self.repository.adauga(student)
        index = self.repository.get_student_dupa_id(1)
        self.assertEqual(index, 0)
        self.assertEqual(self.repository.get_all()[index].get_nume(), "Pop")


if __name__ == "__main__":
    unittest.main()
