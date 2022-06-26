def day_of_year(year, month, day):
        #Vamos a identificar si el año es biciesto
        if year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            #Cambiamos la variable year de int a str para poder 
            #trabajar con los digitos separados
            year = str(year)
            #Ya que la formula para asignar asignar el valor de
            #cada año se basa en el siglo, vamos a usar solo los
            #dos primeros digitos y le vamos a agregar un par de
            #ceros para que cada vez que el usuario ingrese un año
            #saquemos solo el siglo y lo asignemos al algoritmo
            if (int(year[0:2] + "00")) % 400 == 0:
                keyyear = 6
            elif (((int(year[0:2] + "00")) * 2) * 2) % 400 == 0 and (((((int(year[0:2] + "00")) * 2) * 2) / 400) % 2) != 0 and ((int(year[0:2] + "00")) - 100) % 400 == 0:
                keyyear = 4
            elif (int(year[0:2] + "00")) % 200 == 0:
                keyyear = 2
            else:
                keyyear = 0

            #Asignamos el valor de cada mes segun la formula
            if month == 1:
                key_month = 6
            elif month == 2:
                key_month = 2
            elif month == 3:
                key_month = 3
            elif month == 4:
                key_month = 6
            elif month == 5:
                key_month = 1
            elif month == 6:
                key_month = 4
            elif month == 7:
                key_month = 6
            elif month == 8:
                key_month = 2
            elif month == 9:
                key_month = 5
            elif month == 10:
                key_month = 0
            elif month == 11:
                key_month = 3
            elif month == 12:
                key_month = 5

            #Creamos la formula para sacar el valor unico de
            #cada dia segun la variable
            key_day = (day + key_month + int(year[2:5]) + ((int(year[2:5]))/4) + keyyear) % 7
            
            #Creamos un buble while para que cada vez que el
            #el valor unico sea mayor a 6 lo divida en
            while key_day > 6:
                key_day = key_day % 2

            if key_day == 0:
                name_day = "Domingo"
            elif key_day == 1:
                name_day = "Lunes"
            elif key_day == 2:
                name_day = "Martes"
            elif key_day == 3:
                name_day = "Miercoles"
            elif key_day == 4:
                name_day = "Jueves"
            elif key_day == 5:
                name_day = "Viernes"
            elif key_day == 6:
                name_day = "Sabado"

            #Imprimimos el dia
            print(f"El día {day} del mes {month} del año {year} es un {name_day}")

        else:
            year = str(year)
            if (int(year[0:2] + "00")) % 400 == 0:
                keyyear = 6
            elif (((int(year[0:2] + "00")) * 2) * 2) % 400 == 0 and (((((int(year[0:2] + "00")) * 2) * 2) / 400) % 2) != 0 and ((int(year[0:2] + "00")) - 100) % 400 == 0:
                keyyear = 4
            elif (int(year[0:2] + "00")) % 200 == 0:
                keyyear = 2
            else:
                keyyear = 0

            if month == 1:
                key_month = 0
            elif month == 2:
                key_month = 3
            elif month == 3:
                key_month = 3
            elif month == 4:
                key_month = 6
            elif month == 5:
                key_month = 1
            elif month == 6:
                key_month = 4
            elif month == 7:
                key_month = 6
            elif month == 8:
                key_month = 2
            elif month == 9:
                key_month = 5
            elif month == 10:
                key_month = 0
            elif month == 11:
                key_month = 3
            elif month == 12:
                key_month = 5

            key_day = (day + key_month + int(year[2:5]) + ((int(year[2:5]))/4) + keyyear) % 7
            while key_day > 7:
                key_day = key_day % 2
          
            if key_day < 1:
                name_day = "Domingo"
            elif key_day < 2:
                name_day = "Lunes"
            elif key_day < 3:
                name_day = "Martes"
            elif key_day < 4:
                name_day = "Miercoles"
            elif key_day < 5:
                name_day = "Jueves"
            elif key_day < 6:
                name_day = "Viernes"
            elif key_day < 7:
                name_day = "Sabado"
            print(f"El día {day} del mes {month} del año {year} es un {name_day}")

enter_year = int(input("Ingresa un año: "))
enter_month = int(input("Ingresa un mes: "))
enter_day = int(input("Ingresa un dia: "))
day_of_year(enter_year, enter_month, enter_day)