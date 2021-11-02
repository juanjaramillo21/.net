""" import mysql.connector """

def menu():
    print("Select an option: ")
    print("1. Find Multiples of x or y in a range from 1 to n")
    print("2. Find Power number")
    print("3. Make Matrix and sum diagonals")
    print("4. Make Program to access database")
    print("5. Make classes Person, Employee and Customer")

def option1():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    n = int(input("Enter the range number: "))
    sum=0
    for i in range(1,n):
        if (i%x == 0) | (i%y == 0):
            sum = sum+i
    print("The sum is: " + str(sum))

def option2():
    n = int(input("Enter the range number: "))
    for i in range(2,n):
        digits = [int(x) for x in str(i)]
        sum=0
        for l in range (0,len(digits)):
            sum= sum + digits[l]**5
        if (sum == i):
            print(sum)
        
def option3():
    n = int(input("Enter order for the square matrix: "))
    if (n<1):
        print("Invalid order")
        option3()
    else:
        m = 1
        matrix = [[0] * n for _ in range(n)]
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        dir = 0
        while (top <= bottom and left <=right):    
            if dir ==0:
                for i in range(left,right+1):
                    matrix[top][i]=m
                    m+=1
                top +=1
                dir = 1

            elif dir ==1:
                for i in range(top,bottom+1): 
                    matrix[i][right]=m
                    m+=1
                right -=1 
                dir = 2
            
            elif dir ==2:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=m
                    m+=1
                bottom -=1
                dir = 3
            
            elif dir ==3:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=m
                    m+=1
                left +=1
                dir = 0
        print(matrix)
        diag = [matrix[i][i] for i in range(0, len(matrix))]
        diaginv = [matrix[i][~i] for i in range(0, len(matrix))]
        if (n%2 != 0): #si la matriz es impar, eliminar de la segunda diagonal el número de la mitad
            diaginv.remove(matrix[n//2][n//2])
        diags = diag + diaginv
        sumdiags=0
        for i in diags:
            sumdiags+=i
        print("The sum of the diagonals is: "+str(sumdiags))
    
def option4():
    conection = mysql.connector.connect(user='root',password='root',host='localhost',database='reto',port='3306')
    print(conection)
    

menu()
option = int(input("Enter your option: "))


if option==1:
    option1()
elif option==2:
    option2()
elif option==3:
    option3()
elif option==4:
    option4()
else:
    print("Invalid option")
    menu()
    option = int(input("Enter your option: "))



