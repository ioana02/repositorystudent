from Domain.student import Student


class Userinterface:
    def __init__(self, student_service):
        self.__student_service = student_service

    def meniu(self):
        meniu = ""
        meniu += "1. Afiseaza toti studentii\n"
        meniu += "2. Adauga student\n"
        meniu += "3. Sterge student\n"
        meniu += "4. Modifica student\n"
        meniu += "5. Citire din fisier\n"
        meniu += "6. Adauga student in fisier\n"
        meniu += "7. Sterge student in fisier\n"
        meniu += "8. Modifica student in fisier\n"
        meniu += "0. Iesire\n"
        return meniu

    def program(self):
        ruleaza = True
        while ruleaza == True:
            meniul_meu = self.meniu()
            print(meniul_meu)
            comanda = input("Introduceti comanda:")
            if comanda == "1":
                self.ui_afiseaza_studenti()
            elif comanda == "2":
                self.ui_adauga_student()
            elif comanda == "3":
                self.ui_sterge_student()
            elif comanda == "4":
                self.ui_modifica_student()
            elif comanda == "5":
                self.ui_citire_student_fisier()
            elif comanda == "6":
                self.ui_adauga_student_fisier()
            elif comanda == "7":
                self.ui_sterge_student_fisier()
            elif comanda == "8":
                self.ui_modifica_student_fisier()
            elif comanda == "0":
                ruleaza = False
            else:
                print("Comanda gresita! Reincercati!")

    def ui_adauga_student(self):
        try:
            id = int(input("Dati id-ul: "))
            nume = input("Dati numele: ")
            prenume = input("Dati prenumele: ")
            grup = int(input("Dati grupa: "))
            self.__student_service.adauga(id, nume, prenume, grup)
        # except ValueError:
        #     print("Date gresite! Reincercati!")
        except ValueError as e:  # Erori legate de validarea sau existența ID-ului
            print(f"Eroare: {e}")
        except Exception as e:  # Alte erori neprevăzute
            print(f"A apărut o eroare neașteptată: {e}")

    def ui_sterge_student(self):
        try:
            id = int(input("Dati id-ul studentului pe care doriti sa il stergeti:"))
            self.__student_service.sterge(id)
        except ValueError:
            print("Date gresite! Reincercati!")

    def ui_modifica_student(self):
        try:
            id = int(input("Dati id-ul studentului pe care doriti sa il modificiati:"))
            nume_nou = input("Dati numele nou:")
            prenume_nou = input("Dati prenumele nou:")
            grup_nou = int(input("Dati grupul nou:"))
            self.__student_service.modifica(id, nume_nou, prenume_nou, grup_nou)
        except ValueError as e:  # Erori legate de validarea sau existența ID-ului
            print(f"Eroare: {e}")
        except Exception as e:  # Alte erori neprevăzute
            print(f"A apărut o eroare neașteptată: {e}")

    def ui_afiseaza_studenti(self):
        studenti = self.__student_service.get_all()
        if len(studenti) == 0:
            print("Lista de studenti e goala!")
        for student in studenti:
            print(student)

    def ui_citire_student_fisier(self):
        lista_studenti = self.__student_service.get_all()
        for student in lista_studenti:
            print(student)

    def ui_adauga_student_fisier(self):
        try:
            id = int(input("id: "))
            nume = input("nume: ")
            prenume = input("prenume: ")
            grupa = int(input("grupa: "))
            self.__student_service.adauga(id, nume, prenume, grupa)
        except ValueError:
            print("eroare")

    def ui_sterge_student_fisier(self):
        try:
            id = int(input("id: "))
            self.__student_service.sterge(id)
        except ValueError:
            print("eroare")

    def ui_modifica_student_fisier(self):
        try:
            id = int(input("id: "))
            nume = input("nume: ")
            prenume = input("prenume: ")
            grupa = int(input("grupa: "))
            self.__student_service.modifica(id, nume, prenume, grupa)
        except ValueError:
            print("eroare")
