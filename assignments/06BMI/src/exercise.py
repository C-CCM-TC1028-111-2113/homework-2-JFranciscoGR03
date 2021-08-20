def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    while peso<=0 or altura<=0:
        break
    print("Revisa tus datos, alguno de ellos es erróneo.")
    
    imc= peso/(altura**2)

    if imc<20:
        print("PESO BAJO")
    elif 20<=imc<25:
        print("NORMAL")
    elif 25<=imc<30:
        print("SOBREPESO")
    elif 30<=imc<40:
        print("OBESIDAD")
    elif imc>=40:
        print("OBESIDAD MORBIDA")
if __name__=='__main__':
    main()
