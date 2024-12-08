from Domain.student import Student


class StudentService:
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def get_all(self):
        return self.__repository.get_all()

    def adauga(self, id, nume, prenume, grup):
        try:
            student = Student(id, nume, prenume, grup)
            self.__validator.valideaza(student)
            self.__repository.adauga(student)
        except ValueError as e:
            raise ValueError(f"Adăugare eșuată: {e}")

    def sterge(self, id):
        self.__repository.sterge(id)

    def modifica(self, id, nume_nou, prenume_nou, grupa_noua):
        try:
            student_nou = Student(id, nume_nou, prenume_nou, grupa_noua)
            self.__validator.valideaza(student_nou)
            self.__repository.modifica(student_nou)
        except ValueError as e:
            raise ValueError(f"Adăugare eșuată: {e}")

    def sortare_dupa_nume_crecator(self):
        lista_studenti = self.__repository.get_all()
        lista_studenti.sort(key=lambda x: (x.get_nume()))
        return lista_studenti

    def sortare_dupa_id_prenume_descrescatoare(self):
        lista_studenti = self.__repository.get_all()
        lista_studenti.sort(key=lambda x: (x.get_id(), x.get_prenume()), reverse=True)
        return lista_studenti
