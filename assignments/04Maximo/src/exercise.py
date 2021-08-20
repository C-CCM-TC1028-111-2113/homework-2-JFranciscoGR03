def main():
    #escribe tu código abajo de esta línea
    numero1= int(input("Ingresa el primer número: "))
    numero2= int(input("Ingresa el segundo número: "))
    numero3= int(input("Ingresa el tercer número: "))

    if numero1<numero2<numero3:
        print(numero3)
    elif numero2<numero1<numero3:
        print(numero3)
    elif numero1<numero3<numero2:
        print(numero2)
    elif numero3<numero1<numero2:
        print(numero2)
    elif numero2<numero3<numero1:
        print(numero1)
    elif numero3<numero2<numero1:
        print(numero1)


if __name__=='__main__':
    main()
