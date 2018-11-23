import math
import var

#calculates the axial tension strength
def axial(load):
   area = math.pi / 4
   axial = -1 *  load / area
   return axial

#calculates the bending compression strength
def bend(load):
    bending = (load * var.canalOffset * 32) / math.pi
    return bending

#Performs a loop that will iterate through values until a root is found (the root is the value of the diameter)
def calculate(equation):
    #set initial values to allow for iteration
    minDiameter = 5
    zero = 10
    #loops until the value of the funcion using the chosen root is close enough to zero)
    while (zero > 0.001):
       # recalculates the value of diameter 
       minDiameter =  newtons(equation, minDiameter)
       #checks to see what the value of the function is with the new diameter
       zero = check(equation, minDiameter)
    return minDiameter

#uses newton's nethod to determine the x intercept, which is equivallent to the radius of the bone
def newtons(equation, minDiameter):
    # calculates the value of the function and the deriviative of the function, with the current diameter being evaluates
    function = equation[0] * (minDiameter ** 3) - equation[1] * (minDiameter ** 2) - equation[2]
    deriviative = equation[0] * 3  * (minDiameter ** 2) - equation[1] * 2 * minDiameter
    # evaluates x1 = x0 - f(x) / f'(x)
    minDiameter = minDiameter - (function / deriviative)
    return minDiameter

#calculates the value of the value of the function with the newly calculated minimum diameter
def check(equation, minDiameter):
    zero = equation[0] * (minDiameter ** 3) - equation[1] * (minDiameter ** 2) - equation[2]
    return zero

#main program that calls other functions 
def minDiamCalc():
    #calls other functions to make calculations
    appTenStress = var.bodyWeight * 3.5
    a = axial(appTenStress)
    b  = bend(appTenStress)
    equation = [var.ultTenStrength, a, b]
    minDia = calculate(equation)
    return minDia, (a + b)

#calls sub1 and prints the required information
def statementPrinter(minDiameter, tens):
    #Prints the required information, involving the inputted data
    print("\tThe following calculations have been made for users with the following parameters")
    print("\tBody Weight: ", (var.bodyWeight / 9.8), "kg")
    print("\tCanal diameter: ", var.canalDiameter, "mm") 
    print("\tZercanium with a tensile strength:  ", var.ultTenStrength, "MPa")
    print(("\tThe minimum diameter that can be used for this implant is %s mm" % (minDiameter)))
    print(("\tThe applied tensile strength for this implant is %s MPa" % (tens)))
