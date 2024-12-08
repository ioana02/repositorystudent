from Domain.student import Student
from Repository.student_repository import StudentRepository


class StudentRepositoryFile(StudentRepository):
    def __init__(self, nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier

    def adauga(self, student):
        self.get_all()
        super().adauga(student)
        lista_noua = super().get_all()
        self.scrie_in_fisier(lista_noua)

    def sterge(self, id):
        self.get_all()
        super().sterge(id)
        lista_noua = super().get_all()
        self.scrie_in_fisier(lista_noua)

    def modifica(self, student_nou):
        self.get_all()
        super().modifica(student_nou)
        lista_noua = super().get_all()
        self.scrie_in_fisier(lista_noua)

    def get_all(self):
        try:
            f = open(self.__nume_fisier)
            linie = f.readline().strip("\n")
            while linie != "":  # daca linia nu e goala (adica: daca nu am ajuns la finalul fisierului)
                lista_atribute = linie.split(",")  # despartim linia citita folosind separatorul ,
                # lista_atribute va fi o lista ce contine, ca elemente, valorile regasite pe linia curenta
                # primul element din lista_atribute e id-ul
                id = int(lista_atribute[0])  # al doilea element din lista_atribute e numele studentului
                nume = lista_atribute[1]  # al treilea element din lista_atribute este grupa
                prenume = lista_atribute[2]
                grupa = int(lista_atribute[3])
                student = Student(id, nume, prenume, grupa)
                # cream studentul folosind valorile citite din fisier
                if self.get_student_by_id(student.get_id()) == -1:
                    super().adauga(
                        student)  # apelam metoda adauga din clasa parinte (adica din clasa StudentRepository)
                linie = f.readline().strip(
                    "\n")  # citim linia urmatoare pe care o vom verifica si prelucra cand intram din nou in while
            f.close()  # la final, inchidem fisierul deschis
            return super().get_all()

        except IOError:
            print("eroare la deschiderea fisierului" + self.__nume_fisier)

    def scrie_in_fisier(self, lista_studenti):
        try:
            f = open(self.__nume_fisier, "w")  # deschidem fisierul in modul SCRIERE: "write" (de acolo vine "w")
            # din lista noastra de studenti, aducem toti studentii
            for student in lista_studenti:
                # parcurgem fiecare student din lista de studenti
                id = student.get_id()
                nume = student.get_nume()
                prenume = student.get_prenume()
                grupa = student.get_grupa()
                linie = str(id) + ", " + nume + ", " + prenume + ", " + str(
                    grupa) + "\n"  # cream o linie de tipul liniilor pe care le-am citit din
                # fisier (
                # atributele separate prin virgula si \n la final de rand)
                f.write(linie)  # scriem acea linie in fisier
            f.close()  # la final, inchidem fisierul
        except IOError:
            print("eroare la deschiderea fisierului" + self.__nume_fisier)
