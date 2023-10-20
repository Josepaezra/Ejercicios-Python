import PyPDF2


pdfFileObj = open('ucv.pdf', 'rb') #Se abre el PDF
pdfReader = PyPDF2.PdfReader(pdfFileObj) #Se guarda en una variable
# print(len(pdfReader.pages)) #Muestra cuantas paginas tiene el pdf

#for i in range(54, 62):
pageObj = pdfReader.pages[61] #Se obtiene la página
x=pageObj.extract_text()
print(x)
print(type(x))

#aa=x.find("Escuela")
#print(f"La escuela empieza en : {aa}")

#Procedimiento para generar una lista con las cédulas, de la página

numero_personas_venezolanas=x.count("-V-") #Cuenta cuantas veces aparece el string -V- en la página (guardada en el string x)
C=0
Cedulas=[]
for _ in range(numero_personas_venezolanas): #Se itera sobre la cantidad de personas -V-
    
    pos=x.find("-V-", C)+3 #Se obtiene la posición de la cédula dentro del string
    cedula_pos=x[pos:pos+8] #Se obtiene la cédula
    Cedulas.append(cedula_pos) #Se anexa la anterior cédula en la lista
    C=pos+1


print(Cedulas)
nu=len(Cedulas) 
print(f"La cantidad de cédulas es: {nu}")