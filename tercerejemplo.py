def suma(a,b):
    return a+b

def resta(a,b):
    return a-b
while True:
  print("""
     1.suma 
      
     2.resta
      
    3. salir
      """)
  
  opc=int(input("ingrese una opcion:"))
  if opc ==1:
        num1=int(input("ingrese un numero:"))
        num2=int(input("ingrese otro numero:"))
        resultado=(num1 +num2)
        print(f"el resultado es:",resultado)
  elif opc ==2:
        num1=int(input("ingrese un numero:"))
        num2=int(input("ingrese otro numero:"))
        resultado=num1 -num2
        print(f"el resultado es:",resultado)
  elif opc ==3:
        print("saliendo dl programa....")
        break

        