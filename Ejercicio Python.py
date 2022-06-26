#Crear un archivo txt y escribir los numeros del 1 al 250 en el archivo.

archi1=open("datos.txt","w") 
for i in range (1, 251):
    print(i)
    archi1.write(str(i)+"\n")
    
archi1.close() 
