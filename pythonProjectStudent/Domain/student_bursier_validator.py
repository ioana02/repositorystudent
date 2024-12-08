class StudentBursierValidator:
    def valideaza(self, student_bursier):
        erori = []
        if student_bursier.get_tip_bursa() not in ["merit", "sociala"]:
            erori.append("Nu exista alte tipuri de bursa")
        if student_bursier.get_valoare_bursa() > 1500:
            erori.append("Valoarrea bursei nu poate sa depaseasca 1500 de lei")
        if erori:
            raise ValueError("\n".join(erori))
