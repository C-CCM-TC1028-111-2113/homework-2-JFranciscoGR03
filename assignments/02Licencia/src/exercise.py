
def main():
    #Escribe tu código debajo de esta línea
    edad= int(input("Ingresa tu edad: "))
    iden= input("¿Tienes identificación oficial? (s/n): ")

    if edad>=18 and iden=="s":
        print("Trámite de licencia concedido")
    elif edad<18 or iden=="n":
        print("No cumples requisitos")
    elif edad<0 or iden!="s" or iden!="n":
        print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
