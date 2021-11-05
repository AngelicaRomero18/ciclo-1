ciudad= input()#leer una entrada
archivo=open('data.csv', 'r')#abrir el archivo  
matriz=[]#inicialisamos matriz en cero 
for item in archivo:# recorro la matriz
    item = item.rstrip('\n').split(",")# le quitamos los salto de linea y le ponemos comas
    matriz.append(item)# empezamos a llenar la matriz con los datos del archivo
    
count_ciu=0
ingreso=[]# inicialisamos lista en cero     
count_sin=0
count_afro=0
count_ind=0
count_rai=0
count_pal=0
count_git=0
e=0
ccn=0

for j in range(len(matriz)):# recorremos la matriz
    if matriz[j][2]==ciudad:# si la matriz en la posicion 2 en igual a ciudad  entonces:
        if matriz[j][7]== "1": #si la matriz en la posicion 7 es igual a 1 entonces:
            count_ciu+=1 # contador de los que pasan    
            ingreso.append(int(matriz[j] [6]))# empezamos a llenar la lista ingreso con la matriz en la posicion 6
            sumaingreso=0# creamos variable en cero     
            for i in range(len(ingreso)):# recorremos la lista ingreso
                sumaingreso+=ingreso[i]# sumamos los ingreso 
            promingresos=sumaingreso/len(ingreso)# sacamos el promedio de los ingresos: sumaingreso / longitud de ingreso 
            minimo_ingreso=min(ingreso)#sacamos el menor de los ingresos
            maximo_ingreso=max(ingreso)#sacamos el maximo de los ingresos
            if matriz[j][4]=="sin reconocimiento":# si la matriz en la posicion 4 es igual a sin reconocimiento, entonces
                count_sin+=1#cuenteme
            elif matriz[j][4]=="afrodescendiente":
                count_afro+=1
            elif matriz[j][4]=="indigena":
                count_ind+=1
            elif matriz[j][4]=="raizal":
                count_rai+=1
            elif matriz[j][4]=="palenquero":
                count_pal+=1
            elif matriz[j][4]=="gitano":
                count_git+=1
        else:
            ccn+=1
        e+=1
if e>0:
    print(count_ciu)
    print(f"{minimo_ingreso} {maximo_ingreso} {promingresos:.2f}")
    lista_count=[count_afro,count_sin,count_ind,count_rai,count_pal,count_git]
    i=0
    while i<6:
        max_value = max(lista_count)
        if max_value==count_afro and max_value !=0:
            print('afrodescendiente', max_value)
            count_afro='anulado'
        elif max_value==count_git and max_value !=0:
            print('gitano', max_value)
            count_git='anulado'
        elif max_value==count_ind and max_value !=0:
            print('indigena', max_value)
            count_ind='anulado'
        elif max_value==count_pal and max_value !=0:
            print('palenquero', max_value)
            count_pal='anulado'
        elif max_value==count_rai and max_value !=0:
            print('raizal', max_value)
            count_rai='anulado'
        elif max_value==count_sin and max_value !=0:
            print('sin reconocimiento', max_value)
            count_sin='anulado'
        lista_count.remove(max_value)
        i=i+1
    