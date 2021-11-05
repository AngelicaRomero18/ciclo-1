var1=0
var2=0
var3=0
salario=908526


reco_etn=  (input('digite su reconocimiento etnico: '
                '\n Sin_reconocimiento'
                '\n Afrodescendiente'
                '\n Indigena'
                '\n Raizal'
                '\n Palenquero'
                '\n Gitano \n' )).lower()

if reco_etn == "sin_reconocimiento":
 var1=0

elif reco_etn == "afrodescendiente":
 var1=4

elif reco_etn == "indigena":
 var1=5

elif reco_etn == "raizal":
 var1=6
        
elif reco_etn== "palenquero":
 var1=7
        
elif reco_etn == "gitano":
 var1=8
        
else:
 print('Se presento un error')


est_so_eco= int (input('Digite Su Estracto: '
                   '\n 1- Estracto_1'
                   '\n 2- Estracto_2'
                   '\n 3- Estracto_3'
                   '\n 4- Estracto_4'
                   '\n 5- Estracto_5'
                   '\n 6- Estracto_6 \n'))
                                        
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
 print('Se presento un error')


ingresos= float(input('Digite Su Salario: '))

if ingresos <salario:
 var3=15
        
elif ingresos ==salario:
 var3=9
       
elif (salario*2) <= ingresos <=(salario*3):
 var3=7
        
elif ingresos == (salario*4):
 var3=4
       
elif ingresos > (salario*4):
 var3=0
     
else:
 var3=0


resul_final = var1 + var2 + var3

if resul_final  >=25:
    print('El candidato continua en el proceso de seleccion')

else:
    print('El candidato no continuaen el proceso de seleccion')

        
                                    





    