import pandas as pd
from prettytable import PrettyTable
import openpyxl 
factorservi = 0
def init():
    factorservi = float(input("Ingresar factor de servico entre 1 y 3: "))
    if(factorservi >= 1 and factorservi <= 3):
        cal(factorservi)        
    else:
        print("El factor de servicio no es correcto")
        init()

def cal(parametro):
    caudal = float(input("Ingresar caudal: "))
    tentrada = float(input("Ingresar Temp entrada: "))
    tsalida = float(input("Ingresar Temp salida: "))
    consta1 = 1000
    consta2 = 0.0003069

    tamanioDT = round(caudal*(tentrada - tsalida)*parametro*consta1*consta2)

    print("\n El distrito mide ", tamanioDT , '\n')
    chillers(tamanioDT)

def chillers(tdt):
    print("\n Tamaños de chillers Centrífuos y de Absorción 500TR, 750TR, 1000TR \n")
    print("Favor indicar cantidad y lea con detenimiento \n")
    print("__________________________________________________________ \n")
   
    c500 = int(input("Ingrerse cantidad para 500TR centrífugos: "))
    c750 = int(input("Ingrerse cantidad para 750TR centrífugos: "))
    c1000 = int(input("Ingrerse cantidad para 1000TR centrífugos: "))
    aa500 = int(input("Ingrerse cantidad para 500TR Absorción: "))
    a750 = int(input("Ingrerse cantidad para 750TR Absorción: "))
    a1000 = int(input("Ingrerse cantidad para 1000TR Absorción: "))

    #tabla
    tabla = PrettyTable (["c500,","c750","c1000","aa500","a750","a1000"])
    tabla.add_row ([c500,c750,c1000,aa500,a750,a1000])
    print(tabla)    
    #matriz cuando imprime todo sale en columna
    #matriz = [["c500","c750","c1000","aa500","a750","a1000"],[c500,c750,c1000,aa500,a750,a1000]]
    #for fila in matriz:
        #for columna in fila:
            #print (columna)
    #for i in range(len(matriz)):
     #for j in range(len(matriz[i])):
        #print(matriz[i][j])

# Con while y los índices
    #fila = 0

    #while fila < len(matriz):
     #columna= 0
    #while columna < len(matriz[fila]):
        #print(mi_tabla[fila][columna])
        #columna += 1
    #fila += 1
           

    #lista funcional 
    #encabezado
    print("\nc500","   c750  "," c1000 "," aa500 "," a750 " ," a1000\n ")
    #lista
    list = [c500,'-',c750,'-',c1000,'-',aa500,'-',a750,'-',a1000] 
    print(list)


    #Operación centrífugos
    totalc= (500*c500)+(750*c750)+(1000*c1000)
    totala= (500*aa500)+(750*a750)+(1000*a1000)
    totales = totala + totalc

    tmax = tdt + (tdt*0.5) #Se comprueba el tamaño maximo de TR
    if totales<=tdt:
        print("\n Las tecnologías seleccionadas no suministran el tamaño del DT \n")
        print("__________________________________________________________ \n")
        chillers(tdt)
    elif totales >= tmax:
        print("\n Las tecnologías seleccionadas superan el tope del DT")
        print("__________________________________________________________ \n")
        chillers(tdt)
    else:
        centrifugos(totalc)
        absorcion(totala)

def centrifugos(parametro1):
    
    rp=parametro1*0.3190995427365	
    g=(parametro1*511.13199046407)/1000	
    c=(parametro1*0.0035174111853)*(1925000/0.88)	
    o=c*0.03	
   

    capex=parametro1*0.0035174111853	
    ft=capex*1000000	
    e=capex*1700000	
    b=capex*2000000
    crearTablas('centri')

    consta2=1000
    centrifu={
    "Energia":["Red_Publica","Microturbina a gas","Solar fotovoltaica","Energia eolica","Energia biomasa","TR de los chillers de adsorcion es:"],
    "Emisiones co2(TCo2 al mes)": [e, rp, b,ft,c,consta2],
    "Capex(Dolares  Megavatios)":[g,o, b, ft, capex,""],
    "Opex(Do-año)": [ft,rp,e, c,g,""],
             }
    df=pd.DataFrame(centrifu) # para llamar la libreria pd
#linea para exportar datos a excel, y carpeta donde se va a guardar
    df.to_excel ('C:/Users/Sergio/Documents/centrifugos.xlsx',index=False)
    

def absorcion(parametro2):

    g=(parametro2*511.13199046407)/1000		
    c=((parametro2 * 0.0035174111853)*(1925000/0.88))		
    o=c*0.03		
  		


    capex=parametro2*0.0035174111853		
    ft=(capex*1000000)*1.015		
    b=capex*2000000 		
    crearTablas('abso')

   #tabla 2
    TRc=1000
    absorciont={
    "Energia":["Microturbina a gas","Solar termica","Energia biomasa","TR de los chillers de absorcion es"],
    "Emisiones co2(TCo2 al mes)": [g,c,b,TRc],
    "Capex(Dolares  Megavatios)":[g,c,o,""],
    "Opex(Do-año)": [g, capex,b,""],
        }
    dt=pd.DataFrame(absorciont)
    print(dt)
    #linea para exportar datos a excel
    dt.to_excel ('C:/users/Sergio/Documents/absorcion.xlsx')   
    

def crearTablas(resp):
    if resp == 'centri':
        #tabla1 = PrettyTable (["centrifugos"])
        #tabla1.add_row ([centrifugos])
        #print(tabla1)  
        print("\n Tabla Centrífugos")
    
    elif resp == 'abso':
        #tabla2 = PrettyTable (["absorcion"])
        #tabla2.add_row ([absorcion])
        #print(tabla2)  
        print("\n Tabla Absorción")	
        


init()
