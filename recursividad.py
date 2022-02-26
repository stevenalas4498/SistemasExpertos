def Fibonacci(numero):
    if(numero==0):
        return 0
    elif(numero==1):
        return 1
    else:
        return (Fibonacci(numero-1)+Fibonacci(numero-2)) 
num=int(input("Ingrese el numero deseado: "))
for i in range(0, num):
  print(Fibonacci(i))