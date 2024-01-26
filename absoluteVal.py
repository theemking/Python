'''
Write a function, absolute_difference, that takes two numbers as parameters
and returns their absolute difference:
'''

numb= -5
numb1=10
numb2= 10
numb3=5
numb4= 200
numb5=-200

def absoluteVal(num, num2):
    numb = eval(num)
    numb1 = eval(num2)
    return abs(numb - numb1)

def absoluteValTwo(num2, numb3):
    numb2=eval(num2)
    numb3=eval(numb3)
    return abs(numb2 - numb3)

def absoluteDiff(numb4, numb5):
    abd= numb4 - numb5
    return abd

def main():
    print("The absolute value of is: ", abs(numb))
    print("Absolute value: ", abs(numb1))
    print("The absolute value of is: ", abs(numb2))
    print("Absolute value: ", abs(numb3))
    print("The absolute value of is: ", absoluteDiff(numb4, numb5))
    print("Absolute value: ", abs(numb5))

main()