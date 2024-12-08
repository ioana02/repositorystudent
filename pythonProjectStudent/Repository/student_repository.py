class StudentRepository:
    def __init__(self):
        self._lista_studenti = []

    def get_all(self):
        return self._lista_studenti

    def get_student_dupa_id(self, id):
        for i in range(0, len(self._lista_studenti)):
            student_curent = self._lista_studenti[i]
            if student_curent.get_id() == id:
                return i
        return -1

    def get_student_by_id(self, id):
        for i in range(0, len(self._lista_studenti)):
            student_curent = self._lista_studenti[i]
            if student_curent.get_id() == id:
                return student_curent
        return -1

    def adauga(self, student):
        if self.get_student_by_id(student.get_id()) != -1:
            raise ValueError("acest student exisat deja")
        else:
            self._lista_studenti.append(student)

    def sterge(self, id):
        if self.get_student_dupa_id(id) == -1:
            raise ValueError("studentul cu acest id nu exista")
        else:
            index = self.get_student_dupa_id(id)
            self._lista_studenti.pop(index)

    def modifica(self, student_nou):
        id_nou = student_nou.get_id()
        if self.get_student_dupa_id(id_nou) == -1:
            raise ValueError("studentul cu acest id nu exista")
        else:
            index = self.get_student_dupa_id(id_nou)
            self._lista_studenti[index] = student_nou
