#4 Solicite al usuario que ingrese tres nรบmeros, sume los dos primeros y multiplique lasumatoria por el tercero. Muestre por pantalla: El resultado es [resultado].

def addition(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    return num1+num2


def app():
    add1 = input('๐ Ingrese un numero: ')
    add2 = input('๐ Ingrese otro numero: ')
    mul3 = input('๐ Ingrese el tercer numero: ')
    output = f'\nEl resultado es {addition(add1,add2) * int(mul3)}'
    print(output)


if __name__ == '__main__':
    app()
