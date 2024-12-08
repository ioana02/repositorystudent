from Domain.student import Student


class StudentBursier(Student):
    def __init__(self, id, nume, prenume, grup, tip_bursa, valoare_bursa):
        super().__init__(id, nume, prenume, grup)
        self.__tip_bursa = tip_bursa
        self.__valoare_bursa = valoare_bursa

    def get_tip_bursa(self):
        return self.__tip_bursa

    def get_valoare_bursa(self):
        return self.__valoare_bursa

    def set_tip_bursa(self, tip_nou_bursa):
        self.__tip_bursa = tip_nou_bursa

    def set_valoare_bursa(self, valoare_noua_bursa):
        self.__valoare_bursa = valoare_noua_bursa

    def __str__(self):
        return f"{super().__str__()}, Tip Bursă: {self.__tip_bursa}, Valoare Bursă: {self.__valoare_bursa}"
