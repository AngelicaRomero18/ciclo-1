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
reco_etn=True


numero = int(input())
while  count1 < numero:
    count1+=1


    reco_etn=  (input()).strip().lower()

    if reco_etn == "sin reconocimiento":
        var1=0
        count2+=1
     
    elif reco_etn == "afrodescendiente":
        var1=4
        count3+=1
     
    elif reco_etn == "indigena":
        var1=5
        count4+=1
     
    elif reco_etn == "raizal":
        var1=6
        count5+=1
            
    elif reco_etn== "palenquero":
        var1=7
        count6+=1
            
    elif reco_etn == "gitano":
        var1=8
        count7+=1
            
    else:
        var1=0
        
     


    est_so_eco= int (input())
                                                
    if est_so_eco == 1:
        var2=10
                
    elif est_so_eco == 2:
        var2=8
            
    elif est_so_eco == 3:
        var2=6
            
    elif est_so_eco == 4:
        var2=2
            
    elif est_so_eco == 5:
        var2=0
                
    elif est_so_eco == 6:
        var2=0
                
    else:
        var2=0
        if reco_etn == "sin reconocimiento":
            count2-=1
     
        elif reco_etn == "afrodescendiente":
            count3-=1
     
        elif reco_etn == "indigena":
            count4-=1
     
        elif reco_etn == "raizal":
            count5-=1
            
        elif reco_etn== "palenquero":
            count6-=1
            
        elif reco_etn == "gitano":
            count7-=1
            
    

    ingresos= float(input())

    if ingresos <salario:
        var3=15
                
    elif ingresos >= salario and ingresos < 2*salario:
        var3=9
            
    elif ingresos >= 2*salario and ingresos < 4*salario:
        var3=7
                
    elif ingresos >= 4*salario and ingresos < 5*salario:
        var3=4
            
    elif ingresos >= 5*salario:
        var3=0
            
    else:
        var3=0
        if reco_etn == "sin reconocimiento":
            count2-=1
     
        elif reco_etn == "afrodescendiente":
            count3-=1
     
        elif reco_etn == "indigena":
            count4-=1
     
        elif reco_etn == "raizal":
            count5-=1
            
        elif reco_etn== "palenquero":
            count6-=1
            
        elif reco_etn == "gitano":
            count7-=1

    resul_final = var1 + var2 + var3

    if resul_final  >=25:
        count8+=1
    else:
        count8=count8
        

print(count8)
print('Sin reconocimiento', count2,
            '\n Afrodescendiente', count3,
            '\n Indigena', count4,
            '\n Raizal', count5,
            '\n Palenquero', count6,
            '\n Gitano', count7 )
             
                                    





    