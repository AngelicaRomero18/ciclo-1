var1=0
var2=0
var3=0
salario=908526
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
etnico=True


numero = int(input())
while  count1 < numero:
    count1+=1
    
    
   
    entrada = input()
    dato = entrada.split(sep= ",")
    etnico  = dato[0].rstrip().lower()
    estrato = int(dato[1])
    ingreso = int(dato[2])
    

    
    if etnico == "sin reconocimiento":
        var1=0
        count2+=1
        
    elif etnico == "afrodescendiente":
        var1=4
        count3+=1
        
    elif etnico == "indigena":
        var1=5
        count4+=1
        
    elif etnico == "raizal":
        var1=6
        count5+=1
                
    elif etnico == "palenquero":
        var1=7
        count6+=1
                
    elif etnico == "gitano":
        var1=8
        count7+=1
                
    else:
        var1=0
        count9+=1


    if estrato == 1:
        var2=10
                    
    elif estrato == 2:
        var2=8
                
    elif estrato == 3:
        var2=6
                
    elif estrato == 4:
        var2=2
                
    elif estrato == 5:
        var2=0
                    
    elif estrato == 6:
        var2=0
                    
    else:
        var2=0
        count9+=1
        if etnico == "sin reconocimiento":
            count2-=1
        
        elif etnico == "afrodescendiente":
            count3-=1
        
        elif etnico == "indigena":
            count4-=1
        
        elif etnico == "raizal":
            count5-=1
                
        elif etnico == "palenquero":
            count6-=1
                
        elif etnico == "gitano":
            count7-=1
                
        
    if ingreso <salario:
        var3=15
                    
    elif ingreso >= salario and ingreso < 2*salario:
        var3=9
                
    elif ingreso >= 2*salario and ingreso < 4*salario:
        var3=7
                    
    elif ingreso >= 4*salario and ingreso < 5*salario:
        var3=4
                
    elif ingreso >= 5*salario:
        var3=0
                
    else:
        var3=0
        count9+=1
        if etnico == "sin reconocimiento":
            count2-=1
        
        elif etnico == "afrodescendiente":
            count3-=1
        
        elif etnico == "indigena":
            count4-=1
        
        elif etnico == "raizal":
            count5-=1
                
        elif etnico == "palenquero":
            count6-=1
                
        elif etnico == "gitano":
            count7-=1

    resul_final = var1 + var2 + var3

    if resul_final  >=25:
        count8+=1
    else:
        count8=count8
        

print(count8, numero-count8-count9, count9 )
lista=[['Sin reconocimiento', count2],['Afrodescendiente', count3],['Indigena', count4],['Raizal', count5],['Palenquero', count6],['Gitano', count7]]
lista.sort(key = lambda x: x[0], reverse=True, )
lista.sort(key = lambda x: x[1], reverse=True, )

for d in lista:
    print("{} {}".format(*d))
                                        
