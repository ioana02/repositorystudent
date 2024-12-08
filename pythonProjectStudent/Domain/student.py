from Domain.entitate import Entitate


class Student(Entitate):
    def __init__(self, id, nume, prenume, grup):
        super().__init__(id)
        self.__id = id
        self.__nume = nume
        self.__prenume = prenume
        self.__grup = grup

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_prenume(self):
        return self.__prenume

    def get_grupa(self):
        return self.__grup

    def set_id_nou(self, id_s_nou):
        self.__id = id_s_nou

    def set_nume_nou(self, nume_nou):
        self.__nume = nume_nou

    def set_prenume_nou(self, prenume_nou):
        self.__prenume = prenume_nou

    def set_grup_nou(self, grup_nou):
        self.__grup = grup_nou

    def __str__(self):
        return "Student: " + str(self.get_id()) + " nume: " + self.get_nume() + " prenume: " + self.get_prenume() + " grup: " + str(
            self.get_grupa())
