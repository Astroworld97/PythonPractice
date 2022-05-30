import random

def partition(arreglo, primero, ultimo, decision, counter):
    i = primero
    n = ultimo
    if decision == 1:
        pivot = arreglo[primero]
    elif decision == 2:
        pivot = arreglo[ultimo]
        arreglo[primero], arreglo[ultimo] = arreglo[ultimo], arreglo[primero]

    while i < n:
        while arreglo[i] <= pivot and i < ultimo:
            i = i + 1
            counter = counter + 1
        while arreglo[n] >= pivot and n > primero:
            n = n - 1
            counter = counter + 1
        if i < n:
            arreglo[i], arreglo[n] = arreglo[n], arreglo[i]
    arreglo[primero], arreglo[n] = arreglo[n], arreglo[primero]

    return n

def quickSort(arreglo, primero, ultimo, decision):
    if primero < ultimo:
        indice=partition(arreglo, primero, ultimo, decision, counter)
        quickSort(arreglo, indice+1 , ultimo, decision)
        quickSort(arreglo, primero, indice - 1, decision)
    return counter


otra = "si"

while otra == "si":
    counter = 0
    print("ELIJA LA FORMA EN LA QUE QUIERE ESCOGER EL PIVOTE")
    print("1) Primera posicion")
    print("2) Ultima posicion")
    decision = int(input("3) Mediana: \n"))

    again = "si"
    while again == "si":
        numbers=[random.randint(0, 100) for i in range(500)]
        print(numbers)
        print(quickSort(numbers, 0, len(numbers) - 1, decision))
        print(numbers)

        again = input("Desea correr el programa otravez con el pivote en la misa posicion? Si o No?: ").lower()


    otra = input("Desea correr el progama otravez? Si o No?: ").lower()