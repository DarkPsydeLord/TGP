respuesta = "si"
while respuesta != "no":
    #entrada de teclado para numeros
    print("Escribe una clave numerica (solo numeros del 1 al 5) no se aceptan repetidos:")
    numeros = input()
    orden = []#se crea un arreglo para guardar la entrada"

    for num in numeros:
        orden.append(int(num))#se indexan las entradas ya como numeros al arreglo

    #se toma la entrada de la palabra a encriptar
    if numeros.isnumeric() and len(numeros) is 5:
        frase = input("escriba la frase a encriptar:\n")
        frase = frase.replace(" ", "")

    #se valida si se pueden separar por 5 letras si no se indexan x's hasta ser 5
    for number in range(len(frase)):
            largo = len(frase)
            if largo % 5 != 0:
                frase += "x"
            else:
                break

    separa = 5
    # se separa la palabra en bloques de 5
    coleccion = [(frase[i:i + separa]) for i in range(0, len(frase), separa)]
    resultado = ""
    for i in range(len(coleccion)):
        palabra = coleccion[i]
    #se toma la palabra y se reordena de acuerdo a la entrada de numeros de forma ciclica
        for indice in range(len(palabra)):
            resultado += palabra[orden[indice] - 1]
    # resultado
    print(resultado)
    respuesta = input("desea realizar otro calculo (si/no:)\n")