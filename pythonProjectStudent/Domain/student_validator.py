import re


class StudentValidator:
    def valideaza(self, student):
        erori = []
        nume_regex = r"^[A-Z][a-z]+$"
        if not re.match(nume_regex, student.get_nume()):
            erori.append("Numele trebuie sa inceapa cu litera mare si nu poate sa contina caractere speciale")
        if not re.match(nume_regex, student.get_prenume()):
            erori.append("Prenumele nu poate sa inceapa cu litera mare si nu poate sa contina caractere speciale")
        if student.get_grupa() < 0:
            erori.append("Nr nu poate sa fie negativ")
        if len(str(student.get_grupa())) < 3:
            erori.append("Nr de grupa nu poate contine mai putin de 3 cifre")
        if erori:
            raise ValueError("\n".join(erori))
