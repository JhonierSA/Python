
def hello(name):    # definiendo una función
    print("Hola,", name)    # cuerpo de la función


name = input("Ingresa tu nombre: ")

hello(name)    # invocación de la función



def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    
    print("¡Feliz año nuevo!")


