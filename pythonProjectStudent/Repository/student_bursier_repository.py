from Domain import student, student_bursier
from Domain.student_bursier import StudentBursier
from Repository.student_repository import StudentRepository


class StudentBursierRepository(StudentRepository):
    def __init__(self):
        super().__init__()

    def get_all(self):
        return [student for student in self.get_all() if isinstance(student, StudentBursier)]

    def adauga(self, student_bursier):
        if not isinstance(student_bursier, StudentBursier):
            raise ValueError("Doar obiecte de tip StudentBursier pot fi adăugate în acest repository.")
        super().adauga(student_bursier)

    def sterge(self, id):
        student = self.get_student_by_id(id)
        if student == -1:
            raise ValueError(f"Studentul cu ID-ul {id} nu există.")
        if not isinstance(student, StudentBursier):
            raise ValueError(f"Studentul cu ID-ul {id} nu este un StudentBursier.")
        super().sterge(id)

    def modifica(self, student_bursier_nou):
        if not isinstance(student_bursier_nou, StudentBursier):
            raise ValueError("Doar obiecte de tip StudentBursier pot fi modificate.")
        id_bursier = student_bursier_nou.get_id()
        student = self.get_student_by_id(id_bursier)
        if student == -1:
            raise ValueError(f"Studentul cu ID-ul {id_bursier} nu există.")
        if not isinstance(student, StudentBursier):
            raise ValueError(f"Studentul cu ID-ul {id_bursier} nu este un StudentBursier.")
        super().modifica(student_bursier_nou)
