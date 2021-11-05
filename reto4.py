def entrada (N):
    matrizetnico=[]
    N=N
    columnas=7

    for i in range (N):
        matrizetnico.append([0]*columnas)

    for j in range(N):
        entrada=input()
        matriz = entrada.split(sep= " ")
        for c in range(columnas):
            matrizetnico[j][c]=int(matriz[c])
    return matrizetnico      


def comparacion (N, matrizetnico, matrizestrato, matrizingreso):

    var1=0
    var2=0
    var3=0
    salario=908526
    count8=0
    count9=0
    listaP=[]
    for j in range (7):
        count8=0
        for i in range(N):
            if matrizetnico [i][j] == 1:
                var1=0
            elif matrizetnico [i][j] == 2:
                var1=4
            elif matrizetnico [i][j] == 3:
                var1=5
            elif matrizetnico [i][j] == 4:
                var1=6
            elif matrizetnico [i][j] == 5:
                var1=7
            elif matrizetnico [i][j] == 6:
                var1=8
            else:
                var1=0
                count9+=1

            if matrizestrato [i][j] == 1:
                var2=10
            elif matrizestrato [i][j] == 2:
                var2=8                   
            elif matrizestrato [i][j] == 3:
                var2=6                          
            elif matrizestrato [i][j] == 4:
                var2=2                          
            elif matrizestrato [i][j] == 5:
                var2=0                               
            elif matrizestrato [i][j] == 6:
                var2=0                               
            else:
                var2=0
                count9+=1
            
            if matrizingreso [i][j] <salario:
                var3=15
            elif matrizingreso [i][j] >= salario and matrizingreso [i][j] < 2*salario:
                var3=9   
            elif matrizingreso [i][j] >= 2*salario and matrizingreso [i][j] < 4*salario:
                var3=7     
            elif matrizingreso [i][j] >= 4*salario and matrizingreso [i][j] < 5*salario:
                var3=4   
            elif matrizingreso [i][j] >= 5*salario:
                var3=0           
            else:
                var3=0

            resul_final = var1 + var2 + var3
            if resul_final  >=25:
                count8+=1
            else:
                count8=count8
        listaP.append(count8)
    print(f'{listaP[0]} {listaP[1]} {listaP[2]} {listaP[3]} {listaP[4]} {listaP[5]} {listaP[6]}')
       
def imprimirEtnia (lista):
    if lista[0]==1:
        return 'sin reconocimiento'
    elif lista[0]==2:
        return 'afrodescendiente' 
    elif lista[0]==3:
        return 'indigena' 
    elif lista[0]==4:
        return 'raizal' 
    elif lista[0]==5:
        return 'palenquero' 
    elif lista[0]==6:
        return 'gitano'  

def cambiarceros(contador):
    if contador==0:
        contador=1000
    else:
        contador=contador
    return contador

def resultadoMenor (N, matrizetnico):
    lista2=[]
    count_sin2=0
    count_afro2=0
    count_ind2=0
    count_rai2=0
    count_pal2=0
    count_git2=0
    for i in range(7):
        count_sin=0
        count_afro=0
        count_ind=0
        count_rai=0
        count_pal=0
        count_git=0
        for j in range(N):
            if matrizetnico[j][i]==1:
                count_sin+=1
                count_sin2+=1
            elif matrizetnico[j][i]==2:
                count_afro+=1
                count_afro2+=1
            elif matrizetnico[j][i]==3:
                count_ind+=1
                count_ind2+=1
            elif matrizetnico[j][i]==4:
                count_rai+=1
                count_rai2+=1
            elif matrizetnico[j][i]==5:
                count_pal+=1
                count_pal2+=1
            elif matrizetnico[j][i]==6:
                count_git+=1
                count_git2+=1
        count_sin =(cambiarceros(count_sin))
        count_afro =(cambiarceros(count_afro))
        count_ind =(cambiarceros(count_ind))
        count_rai =(cambiarceros(count_rai))
        count_pal =(cambiarceros(count_pal))
        count_git =(cambiarceros(count_git))
        lista=[(1,count_sin), (2,count_afro), (3,count_ind), (4,count_rai), (5,count_pal), (6,count_git)]
        lista.sort(key = lambda x: x[0], reverse=False, )
        lista.sort(key = lambda x: x[1], reverse=False, )
        lista2.append(imprimirEtnia(lista[0]))
    lista1=[(1,count_sin2), (2,count_afro2), (3,count_ind2), (4,count_rai2), (5,count_pal2), (6,count_git2)]
    lista1.sort(key = lambda x: x[0], reverse=False, )
    lista1.sort(key = lambda x: x[1], reverse=False, )
    print(f'{lista2[0]},{lista2[1]},{lista2[2]},{lista2[3]},{lista2[4]},{lista2[5]},{lista2[6]}')
    print(imprimirEtnia(lista1[0]))

def resultadoMayor (N, matrizetnico):
    lista2=[]
    count_sin2=0
    count_afro2=0
    count_ind2=0
    count_rai2=0
    count_pal2=0
    count_git2=0
    for i in range(7):
        count_sin=0
        count_afro=0
        count_ind=0
        count_rai=0
        count_pal=0
        count_git=0
        for j in range(N):
            if matrizetnico[j][i]==1:
                count_sin+=1
                count_sin2+=1
            elif matrizetnico[j][i]==2:
                count_afro+=1
                count_afro2+=1
            elif matrizetnico[j][i]==3:
                count_ind+=1
                count_ind2+=1
            elif matrizetnico[j][i]==4:
                count_rai+=1
                count_rai2+=1
            elif matrizetnico[j][i]==5:
                count_pal+=1
                count_pal2+=1
            elif matrizetnico[j][i]==6:
                count_git+=1
                count_git2+=1
        lista=[(1,count_sin), (2,count_afro), (3,count_ind), (4,count_rai), (5,count_pal), (6,count_git)]
        lista.sort(key = lambda x: x[1], reverse=True, )
        lista2.append(imprimirEtnia(lista[0]))
    lista1=[(1,count_sin2), (2,count_afro2), (3,count_ind2), (4,count_rai2), (5,count_pal2), (6,count_git2)]
    lista1.sort(key = lambda x: x[1], reverse=True, )
    print(f'{lista2[0]},{lista2[1]},{lista2[2]},{lista2[3]},{lista2[4]},{lista2[5]},{lista2[6]}')
    print(imprimirEtnia(lista1[0]))
    

N=int(input())
matrizetnico=entrada(N)
matrizestrato=entrada(N)
matrizingreso=entrada(N)
resultadoMenor(N, matrizetnico)
resultadoMayor(N, matrizetnico)
comparacion(N, matrizetnico, matrizestrato, matrizingreso)

    
