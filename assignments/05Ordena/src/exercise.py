def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    
    if x<y<z:
        print(x)
        print(y)
        print(z)
    elif y<x<z:
        print(y)
        print(x)
        print(z)
    elif x<z<y:
        print(x)
        print(z)
        print(y)
    elif z<x<y:
        print(z)
        print(x)
        print(y)
    elif y<z<x:
        print(y)
        print(z)
        print(x)
    elif z<y<x:
        print(z)
        print(y)
        print(x)
    elif x==y==z:
        print(x)
        print(y)
        print(z)


if __name__=='__main__':
    main()
