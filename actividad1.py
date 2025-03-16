NUMERO1
g=0
p=0

presupuesto = float(input("Ingrese su presupuesto: "))
gastos += float(input("Ingrese el valor de los vegetales: "))
gastos += float(input("Ingrese el valor de la carne: "))
gastos += float(input("Ingrese el valor de las especias: "))

if gastos == presupuesto:  
    print("Compra exitosa, dinero restante $0.")
    
elif gastos > presupuesto:
    print(f"No puede realizar la compra, le hacen falta ${gastos-presupuesto}.")
else:
    gastos += float(input("Ingrese el valor de las frutas: "))
    if gastos > presupuesto:
        print(f"No puede realizar la compra, le hacen falta ${gastos-presupuesto}.")
    elif gastos == presupuesto:  
        print("Compra exitosa, dinero restante $0.")
    else:
        print(f"Compra exitosa, dinero restante ${presupuesto-gastos}.")



 NUMERO2
   
 costodelic= 0
totall = 0
pr = 0

while pr <= 0:
    pr = int(input("Ingrese su presupuesto: "))
    if pr <= 0:
        print("Cantidad invalida.")
while costodelic <= 0:
    costodelic = int(input("Ingrese el costo de la licencia: "))
    if costodelic <= 0:
        print("Cantidad invalida.")
while totall <= 0:       
    totall = int(input("Ingrese el numero de licencias que quiere comprar: "))
    if totall <= 0:
        print("Cantidad invalida.")
costo_total = costodelic*totall
if costo_total > pr:
    print(f"No puede efectuar la compra.\nPresupuesto: {pr}\nCosto total: {costo_total}")
elif costo_total == pr:
    print(f"Compra exitosa.\nLicencias extra: 0")
else:
    restante = pr-costo_total
    licencias_extras = restante//costodelic
    print(f"Compra exitosa.\nDinero restante: {restante}\nLicencias extras: {licencias_extras}")       


NUMERO3

total = int(input("Ingresa el número total de estudiantes: "))
integrantes = int(input("¿Cuantos integrantes debe tener cada grupo?\n-"))
if total <= 0 or integrantes <= 0:
    print("Datos invalidos.")
    sys.exit(0)
grupos_completos = total // integrantes
if total % integrantes == 0:
    print(f"Se pueden formar {grupos_completos} grupos de {integrantes} estudiantes.")
else:
    estudiantes_extras = total-(grupos_completos*integrantes)
    print(f"Se pueden formar {grupos_completos} grupos de {integrantes} estudiantes\nEstudiantes que sobran: {estudiantes_extras}")

NUMERO4
 
lapicesM = 32
total_estudiantes = int(input("Ingresa el número de estudiantes: "))
if total_estudiantes <= 0:
    print("Datos invalidos.")
    sys.exit(0)
if total_estudiantes > lapicesM:
    print("Hay más estudiantes que lapices.")
    sys.exit(0)
lapices_restantes = int(lapicesM % total_estudiantes)
print(f"Lapices por estudiante: {lapicesM//total_estudiantes}")
print(f"Lapices que sobran: {lapices_restantes}")


NUMERO5

lado = float(input("Ingrese el valor del lado: "))
print(f"Area = {lado**2}")
#EN CASO DE SER UNA FIGURA DIFERENTE IGUAL SERIA EL PROCESO


NUMERO6
#SE PIDE EL NOMBRE  DE EL USUARIO PARA PODER SER REGISTRADO 
nombredelusuario = input("ingrese su nombre")
if len(nombre) < 3 o len(nombre) > 8 :
    print (" su nombre no esta bien, revise las condiciones impuestas para ser valido ")
    
 else 
 print (f"bienvenido , {nombredelusuario.upper()}.")    


NUMERO7

comentario = input("Ingrese el comentario: ").lower()
repeticiones = comentario.count("excelente")
print(f"comentario modificado\n-{comentario.strip()}\n Veces que se repitioa \"Excelente\": {repeticiones}.")


NUMERO8

articulo = input("Ingrese el articulo: ").strip()
articulo = articulo.lower().replace("tegnologia antigua", "tegnologia de punta")
print(articulo.split("."))

#SE HIZO USO DE MODIFICADORES DE CADENA DE TEXTO PARA PODER "EDITAR LAS PALABRAS"

NUMERO9

while True: #BOOLEAN
    codigo = input("Ingrese su codigo: ").strip().upper()
    if codigo.startswith("PRO"):
        print("Código válido")
    else:
        print("Código inválido")
