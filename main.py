#define the functions needed: add, sub, mul, div
#print options to the user
#ask the values 
#call the functions
#while loop to continue the program until the user want to exit 
def add(a,b):
    answer = a+b
    print(str(a) + '+' +str(b) + '=' + str(answer))
    
def sub(a, b):
    answer = a - b
    print(str(a) + '-' +str(b) + '=' + str(answer))

def mul(a, b):
    answer = a*b
    print(str(a) + 'x' +str(b) + '=' + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + '/' +str(b) + '=' + str(answer))

def sqr(a):
     answer = a**2
     print(str(a) + '^2 '+ '=' + str(answer))

def cube(a):
    answer = a**3
    print(str(a) + '^3 '+ '=' + str(answer))

def sqrroot(a):
    answer = a**0.5
    print(str(a) + '^1/2 ' +'=' + str(answer))

def cuberoot(a):
    answer = a**0.33333
    print(str(a) + '^1/3' + '=' + str(answer))

print("A.Addition")  
print('B.Subtraction')
print('C.Multiply')
print('D.Division')
print('E.Square')
print('F.Cube')
print('G.Square root')
print('H.Cube root')
print('I.exit')

while True:

    choice = input('Enter Your Choice.').lower()


    if choice == 'a':
        print('Addition')
        a = int(input('Enter first number. '))
        b = int(input('Enter second number. '))
        add(a,b)
        continue
    elif choice == 'b':
        print('Subtraction')
        a = int(input('Enter first number. '))
        b = int(input('Enter second number. '))
        sub(a,b)
        continue
    elif choice == 'c':
        print('Multiply')
        a = int(input('Enter first number. '))
        b = int(input('Enter second number. '))
        mul(a,b)
        continue
    elif choice == 'd':
        print('Division')
        a = int(input('Enter first number. '))
        b = int(input('Enter second number. '))
        div(a,b)
        continue
    elif choice == 'e':
        print('Square')
        a = int(input('Enter number. '))
        sqr(a)
        continue
    elif choice == 'f':
        print('Cube')
        a = int(input('Enter number. '))
        cube(a)
        continue
    elif choice == 'g':
        print('Square root')
        a = int(input('Enter number. '))
        sqrroot(a)
        continue
    elif choice == 'h':
        print('Cube root')
        a = int(input('Enter number. '))
        cuberoot(a)
        continue
    else:
        print('Program ended.')
        quit()

