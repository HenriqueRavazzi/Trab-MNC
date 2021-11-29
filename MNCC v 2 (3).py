"""
Created on Wed Aug  7 09:49:01 2019

@author: Martins, Helamã Moreira; Tavares, Henrique Ravazzi
"""

import math as m
import numpy as np

def MenuPrincipal(): 
    print("---------------Menu----------------")
    print("   Selecione a operação desejada   ")
    print("Operação 1: Cálculo de raízes      ")
    print("Operação 2: Sistema de Eq. Lineares")
    print("Operação 3: Interpolação           ")
    print("Operação 4: Integração Numérica    ")
    print("Operação 5: Eq. Dif. Ordinárias    ")
    print("Operação 0: Encerrar               ")
    
def MenuRaiz():
    print("---------------Menu----------------")
    print("Método 1: Bissecçao                ")
    print("Método 2: Newton                   ")
    print("Método 3: Secantes                 ")
    print("Método 0: Voltar                   ")
    
def FunçãoDeAnálise(x) : #Caso deseje alterar a função análisada, realize a alteração aqui!!
    f = x**4 -8
    return f
    
def FunçãoDerivada(x): #Derivada da função de análise, deve ser corrigida sempre que a FA for alterada.
    fd = 4*x**3
    return fd

def Bissecção():
     
     a = int(input("Insira o menor valor do intervalo de análise: "))
     b = int(input("Insira o maior valor do intervalo de análise: "))
     xk = 0
     xk1 = 1
     cp = int(input("Defina o critério de parada(grau de precisão): ")) #Critério "simplificado"
     cr = 10**(-cp) #Critério aplicado
     CritérioDeParada = 1 # Primeiro calculo do critério de parada

     
     if FunçãoDeAnálise(a)*FunçãoDeAnálise(b) >= 0 :
         print("O intervalo inserido é inválido")
         print("O produto f(a)*f(b) deve ser menor que zero")
         MenuPrincipal()
     else:
         while (CritérioDeParada >= cr) :
             xk = (a+b)/2
             g = FunçãoDeAnálise(a) * FunçãoDeAnálise(xk) 
             CritérioDeParada = abs(xk1 - xk)/abs(xk1)
             if g > 0:
                 a = xk
                 if FunçãoDeAnálise(a)*FunçãoDeAnálise(b) >= 0 :
                     print("O intervalo inserido é inválido")
                     print("O produto f(a)*f(b), é igual a zero para o valor a=", a)
                     break
             elif g < 0 :
                 b = xk 
                 if FunçãoDeAnálise(a)*FunçãoDeAnálise(b) >= 0 :
                     print("O intervalo inserido é inválido")
                     print("O produto f(a)*f(b) é igual a zero para o valor b =", b)
                     break
             xk1 = xk 
             
             if xk1 < 0 :
                 pr = cp +1
             elif (xk1 <= 10)or (-10<xk1<=0):
                 pr = cp + 2
             elif (xk1 <= 100)or (-100<xk1<= -10):
                 pr = cp +3
             elif (xk1 <= 1000) or (-1000<xk1<= -100):
                 pr = cp +4
             elif (xk1 <= 10000) or (-10000<xk1<= -1000):
                 pr = cp +5
             elif (xk1 <= 100000)or (-100000<xk1<= -10000):
                 pr = cp +6    
         
         print("\2")   
         print("A raiz da função, segundo o método da bissecção é :")
         print(format(xk1, '.%dg' % pr))
         print("\2")

    
      
     w = input("\nPressione enter para continuar")
         
         
def Newton():
    xk = int(input("Insira o ponto de análise: ")) #x0
    cp = int(input("Insira o critério de parada: "))#grau de precisão
    cr = 10**(-cp) #Critério "Real"
    CritérioDeParada = 1
    
    if FunçãoDerivada(xk) == 0 :
        print("A função derivada é igual a zero, por favor corrija função")
    else:
        
    
        while CritérioDeParada >= cr :
            if FunçãoDerivada(xk) == 0 :
                print("Derivada da função é igual a zero pra xk=", xk)
                print("Impossível prosseguir!")
                break
            else:
                xkb = xk - FunçãoDeAnálise(xk)/FunçãoDerivada(xk)
                CritérioDeParada = abs(xkb - xk)/abs(xkb)
                xk = xkb
            
            
            
            if xk < 0 :
                pr = cp +1
            elif (xk <= 10)or (-10<xk<=0):
                pr = cp + 2
            elif (xk <= 100)or (-100<xk<= -10):
                pr = cp +3
            elif (xk <= 1000) or (-1000<xk<= -100):
                pr = cp +4
            elif (xk <= 10000) or (-10000<xk<= -1000):
                pr = cp +5
            elif (xk <= 100000)or (-100000<xk<= -10000):
                pr = cp +6 
                
                
                
        print("\2")
        print("A raiz da equação para o critério de parada ",cr," é: ")
        print(format(xk, '.%dg' % pr))
    w = input("\nPressione enter para continuar")
        
def Secante():
    x1 = float(input("Coloque um valor para o x1: "))
    x2 = float(input("Coloque um valor para o x2: "))
    cp = int(input("Coloque um valor critério de parada: "))
    cr = 10**(-cp)
    pr = cp*2 -1
    CritérioDeParada = 1  
    
    
    while CritérioDeParada >= cr :
        if FunçãoDeAnálise(x2) - FunçãoDeAnálise(x1):
            print("Erro, F(a) - F(b) = 0")
            break
        else:   
            xk =( x1 * FunçãoDeAnálise(x2) - x2 * FunçãoDeAnálise(x1))/(FunçãoDeAnálise(x2) - FunçãoDeAnálise(x1))
            CritérioDeParada = abs(xk - x2)/abs(xk)
            x1 = x2
            x2 = xk
        
            if xk < 0 :
                pr = cp +1
            elif (xk <= 10)or (-10<xk<=0):
                pr = cp + 2
            elif (xk <= 100)or (-100<xk<= -10):
                pr = cp +3
            elif (xk <= 1000) or (-1000<xk<= -100):
                pr = cp +4
            elif (xk <= 10000) or (-10000<xk<= -1000):
                pr = cp +5
            elif (xk <= 100000)or (-100000<xk<= -10000):
                pr = cp +6    
      
        print("A raiz da função, segundo o método das Secantes é :")
        print(format(xk, '.%dg' % pr))
        print("\2")
    w = input("\nPressione <enter> para continuar")             

def Menu2():
    print("---------------Menu----------------")
    print("Método 1:Eliminação de Gauss       ")
    print("Método 2:Decomposição LU           ")
    print("Método 3:Jacobi-Richardson         ")
    print("Método 4:Gauss-Seidel              ")
    print("Método 0: Voltar                   ")

def matrizA():
    A = [[-1,0,4],[1,0,-2],[1,-1,0]]
    return A
def matrizB():
    B = [18,-5, 5]
    return B
def Gauss():
    a = matrizA()
    b = matrizB()
    n = len(a)
    x = np.zeros((n))

    for k in range(0 ,n-1, 1):
        if a[k][k] == 0 :
            print("Erro,ao menos 1 dos valores a[k][k] é zero! Por favor, corrija a matriz e tente novamente!")
            print("k=",k)
            w = input("\nPressione <enter> para continuar")
            Menu2()
        else: 
            for i in range (k+1 , n , 1):
                aux = a[i][k]
                b[i] = b[i] - b[k]*(aux / a[k][k])
                for j in range(k , n , 1):
                    a[i][j] = a[i][j] - a[k][j]*(aux/ a[k][k])
    
    for i in range ( n-1 , -1 ,-1):
        soma = 0
        for j in range (i+1 , n , 1):
            soma = a[i][j] *x[j] 
            
        x[i] = (b[i] - soma)/ a[i][i]
        print("x[%d]= "%(i+1), x[i])
        
      
    print(np.array(a))
    print("b=",np.array(b))

    w = input("\nPressione <enter> para continuar") 
    
def LU():
    a = matrizA()
    b = matrizB() 
    n = len(b)
    
    L = np.array([[0.0] * n for i in range(n)])
    U = np.array([[0.0] * n for i in range(n)])
    
    
    for j in np.arange(n-1):  
        for i in np.arange(j+1,n):  
            L[i,j] = U[i,j]/U[j,j]  
            for k in np.arange(j+1,n):  
                U[i,k] = U[i,k] - L[i,j]*U[j,k]  
            U[i,j] = 0
                
    print("\nL = ")
    print("\n", L)
    print("\nU = ")
    print("\n", U)


    print("Matriz iterada:")
    print(np.array(a))
    for i in range(1 , n , 1):
        s = 0
        for k in range (0 , i , 1):
            s = s + a[i][k]*b[k]
        b[i] = b[i] - s
   
    print("Raizes:", b)
    
    for i in range (n-1 , -1 , -1):
        s = 0
        for k in range (i+1 , n , 1):
            s = s + (a[i][k] * b[k])
        b[i] = (b[i] - s)/ a[i][i]



        print("x[%d]= " %( i+1 ) , b[i])
    W = input("\nPressione <enter> para continuar") 
    

def Jacobi():
    a = matrizA() 
    b = matrizB()
    n=len(b)
    x0=np.zeros(n)
    x=np.zeros(n)
    cp=int(input("Grau de precisão(valor inteiro): "))
    cr=10**(-cp)
    it = int(input("Insira a quantidade de iterações máxima:" ))
    IT = 1
    while IT <= it:
        x0 = np.copy(x)
        for i in range (0,n,1):
            soma=0
            for j in range(0,n,1):
                if i!=j:
                    soma=soma+(a[i][j]*x0[j])
            x[i]=((+b[i]-soma)/a[i][i])
#            print("IT=",IT)
#            print("i=",i)
#            print("j=",j)
#            print("s=",soma)
            IT = IT + 1
            if IT == it:
                print("Número de iterações excedido!")
                print("O procedimento falhou!")
        print(x0)
        if abs(max(x0-x))/(abs(max(x)))< cr:
            print(x0)
            break
    

    W = input("\nPressione <enter> para continuar")
    
        
def GS():
    a = matrizA() 
    b = matrizB()
    n=len(b)
    x=np.zeros(n)
    cp=int(input("Grau de precisão(valor inteiro): "))
    cr=10**(-cp)
    it = int(input("Insira a quantidade de iterações máxima:" ))
    IT = 1
    while IT <= it:
        for i in range (0,n,1):
            soma=0
            for j in range(0,n,1):
                if i!=j:
                    soma=soma+(a[i][j]*x[j])
            x[i]=((+b[i]-soma)/a[i][i])
            print("IT=",IT)
            print("i=",i)
            print("j=",j)
            print("s=",soma)
         
            IT = IT + 1
            if IT == it:
                print("Número de iterações excedido!")
                print("O procedimento falhou!")
    if abs(max(x-x))/(abs(max(x)))< cr:
        print(x)
        
        
            
    W = ("\nPressione <enter> para continuar")
   
        
    
def Menu3():
    print("---------------Menu----------------")
    print("Método 1:Lagrange                  ")
    print("Método 2:Newton                    ")
    print("Método 0: Voltar                   ")

 

def Lagrange():
    x =np.array([1, 3, 4, 5])
    y = np.array([0, 6, 24, 60])
    n1 = len(x)
    n2 = len(y)

    if n1 != n2 :
        print("f e f(x) devem ter a mesma quantiade de valores! Por favor, corrija a tabela!")
        w = ("\nPressione <enter> para continuar")
        MenuPrincipal() 
        
    else: 
        X = float(input("Insira o valor de X para o qual deseja obter a imagem P(x):"))
        S = 0

        for k in range(0, n1):
            P=1
            for j in range(0, n1):
                if j != k:
                    P = P *((X - x[j])/(x[k] - x[j]))
            S = S + y[k]*P
        print("Pn(x) = ", S)
        

                
def INewton():
    x =np.array([-1,0,3])
    f = np.array([15,8,-1])
    n1 = len(x)
    n2 = len(f)

    if n1 != n2 :
        print("f e f(x) devem ter a mesma quantiade de valores! Por favor, corrija a tabela!")
        w = ("\nPressione <enter> para continuar")
        MenuPrincipal()
    else:
        for i in range(1, n1):
            for j in range(n1-1, i-1, -1):
                f[j] = (f[j] - f[j-1])/(x[j] - x[j-i])
            print(f)
            

    X = float(input("Insira o valor de X para o qual deseja obter a imagem P(x):"))
    S = 0

    for i in range(0, n1):
        P=1
        for j in range(0, i):
            P = (X-x[j])*P
        S = S + f[i]*P
    print(S) 
    
    
    
    

def Menu4():
    print("---------------Menu----------------")
    print("Método 1:Trapézio                  ")
    print("Método 2:1/3 de Simpson            ")
    print("Método 3:3/8 de Simpson            ")
    print("Método 0: Voltar                   ")

def FunçãoMenu4(x):
    return (m.e**(-x))*m.sin(x)
def Trapézio():
    a = float(input("Menor ponto utilizado:"))
    b = float(input("Maior ponto utilizado:"))
    n = int(input("Número de pontos considerados:"))
    H = b-a
    h = H/n
    
    if  a > b:
        print("Os intervalos inseridos são inválidos, a < b")
        w = ("\nPressione <enter> para continuar")
        Trapézio()
    elif n < 0 :
        print("O número de pontos deve ser um valor inteiro e postivo")
        w = ("\nPressione <enter> para continuar")
        Trapézio()
    S = FunçãoMenu4(a)
    for i in range(1, n):
        
        S = S + 2*(FunçãoMenu4(a + i*h))
    S = S + FunçãoMenu4(b)
    In = h/2 * S
    print(In)
    

def Simpson3():
    a = float(input("Insira o menor valor do intervalo: "))
    b = float(input("Insira o maior valor do intervalo: "))
    n= int(input("insira o passo:"))
    h = (b-a)/n
    
    if (n%2) == 0 :
        
        S = FunçãoMenu4(a) + FunçãoMenu4(b)
        for i in range(1, n, 2):
            S = S + 4*FunçãoMenu4(a + i*h)
        for i in range(2,n-1, 2):
            S = S + 2*FunçãoMenu4(a + i*h)
        I = (h/3) * S  
    
        print(I)
        
    else:
        print("Erro")
    
    
def Simpson8():
    
    a = float(input("Insira o menor valor do intervalo: "))
    b = float(input("Insira o maior valor do intervalo: "))
    n= int(input("insira o passo:"))
    h = (b-a)/n
    
    if  (n%3) == 0 :
        
        S = FunçãoMenu4(a) + FunçãoMenu4(b)
        for i in range(1, n-1, 3):
            S = S + 3*(FunçãoMenu4(a+i*h) + FunçãoMenu4((a+(i*h)+h)))
        for i in range(3, n-2, 3):
            S = S + 2*FunçãoMenu4(a + i*h)
        I = (3*h/8) * S  
    
        print(I)
        
    else:
        print("Erro")
        
    

def Menu5():
    print("---------------Menu----------------")
    print("Método 1:Runge-Kutta 4ª Ordem      ")
    print("Método 0: Voltar                   ")
    
def funçãoRK(x,y):
    return x - y + 2    
    
    
def RungeKutta():
    xn = float(input("Qual o limite inferior que deseja :"))
    yn = float(input("Qual o valor de y0 :"))
    h = float(input("Qual o tamanho do passo h :"))
    while h<= 0 :
        h = float(input("Qual o valor de h maior que 0 :"))
    xN = float(input("Qual o limete superior que deseja :"))
    N = (xN-xn)/h
    print("y[0] = %.10f" %yn)
    if h*N == xN-xn :
        for n in np.arange ( 0 , N , 1):
            k1 = funçãoRK(xn , yn)
            k2 = funçãoRK(xn + h/2 , yn + (h*k1)/2)
            k3 = funçãoRK(xn + h/2 , yn + (h*k2)/2)
            k4 = funçãoRK(xn + h , yn + h*k3)
            yn = yn + (h/6)*(k1+(2*k2)+(2*k3)+k4)
            xn = xn + h
            print("y[%d] = %.15f" %(n+1 , yn))
            print("xn =" ,xn)
            print("k1=",k1)
            print("k2=",k2)
            print("k3=",k3)
            print("k4=",k4)
    else :
        print("Você colocou valores errados , por favor coloque valores que  façam N*h= xN-x0")
    
        

    

    
while True :
    MenuPrincipal() 
    Operação = int(input("Insira a operação Desejada:"))
    
    if (Operação < 0 or Operação > 6):
        print("A operação selecionada é inválida!")
        print("Por favor, selecione uma opção válida!")
        w = input('Pressione <enter> para continuar')
    elif Operação == 0 :
        print("\n" * 50)
        print("Programa encerrado!")
        break

    elif Operação == 1 :
        MenuRaiz()
        Método = int(input("Selecione o método: "))
        if Método == 1 :
            Bissecção()
        elif Método == 2:
            Newton()
        elif Método == 3:
            Secante()
        elif Método == 0:
            MenuPrincipal()
        else: 
            print("Opção inválida! Tente novamente")
            MenuRaiz()
        
    elif Operação == 2 :
        Menu2()
        Método = int(input("Selecione o método: "))
        if Método == 1:
            Gauss()
        elif Método == 2 :
            LU()
        elif Método == 3:
            Jacobi()
        elif Método == 4:
            GS()
        elif Método == 0:
            MenuPrincipal()
        else: 
            print("Opção inválida! Tente novamente")
            Menu2()
            
            
    elif Operação == 3 :
        Menu3()
        Método = int(input("Selecione o método: "))
        if Método == 0:
            MenuPrincipal()
        elif Método == 1 :
            Lagrange()
        elif Método == 2:
            INewton()
            
    elif Operação == 4 :
        Menu4()
        Método = int(input("Selecione o método: "))
        if Método == 0:
            MenuPrincipal()
        elif Método == 1:
            Trapézio()
        elif Método == 2:
            Simpson3()
        elif Método == 3:
            Simpson8()
       
            
            
    elif Operação == 5 :
        Menu5()
        Método = int(input("Selecione o método: "))
        if Método == 1:
            RungeKutta()
        elif Método == 0:
            MenuPrincipal()
        
