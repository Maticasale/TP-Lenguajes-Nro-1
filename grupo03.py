def calculator(input_operation):
    
    operation = input_operation
    
    Output = eval(''.join([str(x) for x in operation]))

    aux = 0
    pila=[]
    b=0
    operacion = [c for c in operation]

    tope = len(operacion)

    while aux < tope:
        b=0
        if operacion[aux] == "(":
            aux = aux + 1
            while operacion[aux] != ")" and b==0:
                if operacion[aux] == "(":
                    pila = []
                    b=1
                    aux=aux-1
                else:
                    pila.append(operacion[aux])
                    aux=aux+1
            if operacion[aux] == ")":
                break;
        aux=aux+1

    if pila == []:
        x=0
        while x < len(operacion):
            pila.append(operacion[x]) 
            x = x + 1

    operacionP = [c for c in pila]

    i = 4
    operacion = []
    primer=[]
    aux1=0
    p = 0
    var = ""

    tope = len(operacionP)

    while p < tope:
        if operacionP[p] == "+" or operacionP[p] == "-" or operacionP[p] == "/" or operacionP[p] == "(" or operacionP[p] == ")":
            operacion.append(operacionP[p])
            p = p + 1
        else:
            if operacionP[p] == "*":
                if operacionP[p+1] == "*":
                    operacion.append("**")
                    p = p + 2
                else:
                    operacion.append("*")
                    p = p + 1
            else:
                while operacionP[p].isnumeric():
                    var = var + operacionP[p]
                    p = p + 1
                    if p == tope:
                        break
                if var != "":
                    operacion.append(var)
                    var = ""

    tope = len(operacion)

    while aux1 < tope-1 and i != 1:
        if operacion[aux1] == "(" and i > 1:
            primer.clear()
            aux1 = aux1 + 1
            primer.append(operacion[aux1])
            aux1 = aux1 + 1
            primer.append(operacion[aux1])
            aux1 = aux1 + 1
            primer.append(operacion[aux1])
            i = 1
            break
        else:
            aux1 = aux1 + 1
            if operacion[aux1] == "**":
                primer.clear()
                primer.append(operacion[aux1-1])
                primer.append(operacion[aux1])
                primer.append(operacion[aux1+1])
                aux1 = aux1 + 1
                i = 2
            if operacion[aux1] == "*" and i > 2:
                primer.clear()
                primer.append(operacion[aux1-1])
                primer.append(operacion[aux1])
                primer.append(operacion[aux1+1])
                aux1 = aux1 + 1
                i = 3
            if operacion[aux1] == "/" and i > 2:
                primer.clear()
                primer.append(operacion[aux1-1])
                primer.append(operacion[aux1])
                primer.append(operacion[aux1+1])
                aux1 = aux1 + 1
                i = 3
            if operacion[aux1] == "+" and i > 3:
                primer.clear()
                primer.append(operacion[aux1-1])
                primer.append(operacion[aux1])
                primer.append(operacion[aux1+1])
                aux1 = aux1 + 1
                i = 4
            if operacion[aux1] == "-" and i > 3:
                primer.clear()
                primer.append(operacion[aux1-1])
                primer.append(operacion[aux1])
                primer.append(operacion[aux1+1])
                aux1 = aux1 + 1
                i = 4

    x=0
    while x < len(primer):
            var = var + primer[x] 
            x = x + 1

    Resultado=[]
    Resultado.append(var)
    Resultado.append(Output)
    print(Resultado)

input_operation = ""
input_operation = input("ingrese operacion:")

calculator(input_operation)