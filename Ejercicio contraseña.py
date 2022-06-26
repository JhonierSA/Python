contraseña = input("Ingresa una contraseña: ")
contraseña = contraseña.lower()
while True:
    confirmPW = input("Confirma la contraseña: ")
    confirmPW = confirmPW.lower()
    if confirmPW == contraseña:
        print("Confirmacion correcta")
        print(f"Tu contraseña es {contraseña}")
        break
    else:
        print("La contraseña es incorrecta")
