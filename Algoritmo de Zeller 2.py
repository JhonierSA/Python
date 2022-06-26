def dia_de_la_semana(dd, mm, aaaa):
    a = int((14 - mm) / 12)
    y = aaaa - a
    m = int(mm + (12 * a) - 2)
    d = int(dd + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
    return d


def nombre_de_dia(numero_dia):
    return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"][numero_dia]


def main():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    numero_dia = dia_de_la_semana(dia, mes, anio)
    dia = nombre_de_dia(numero_dia)
    print(f"El día es {dia}")


main()