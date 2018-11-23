import math
import var

#calculates the axial tension strength
def axial(load):
   area = math.pi / 4
   axial = -1 *  load / area
   return axial

#calculates the bending compression strength
def bend(load):
    bending = (load * var.canal_offset * 32) / math.pi
    return bending

#Performs a loop that will iterate through values until a root is found (the root is the value of the diameter)
def calculate(equation):
    #set initial values to allow for iteration
    min_diameter = 5
    zero = 10
    #loops until the value of the funcion using the chosen root is close enough to zero)
    while (zero > 0.001):
       # recalculates the value of diameter 
       min_diameter =  newtons(equation, min_diameter)
       #checks to see what the value of the function is with the new diameter
       zero = check(equation, min_diameter)
    return min_diameter

#uses newton's nethod to determine the x intercept, which is equivallent to the radius of the bone
def newtons(equation, min_diameter):
    # calculates the value of the function and the deriviative of the function, with the current diameter being evaluates
    function = equation[0] * (min_diameter ** 3) - equation[1] * (min_diameter)  - equation[2]
    deriviative = equation[0] * 3  * (min_diameter ** 2) - equation[1]
    # evaluates x1 = x0 - f(x) / f'(x)
    min_diameter = min_diameter - (function / deriviative)
    return min_diameter

#calculates the value of the value of the function with the newly calculated minimum diameter
def check(equation, min_diameter):
    zero = equation[0] * (min_diameter ** 3) - equation[1] * (min_diameter) - equation[2]
    return zero

#main program that calls other functions 
def minDiam_calc():
    #calls other functions to make calculations
    load = var.body_weight * 3.5
    a = axial(load)
    b  = bend(load)
    equation = [var.ultTen_strength, a, b]
    min_dia = calculate(equation)
    app_tens = a / (min_dia ** 2) + b / (min_dia ** 3)
    return min_dia, app_tens

#calls sub1 and prints the required information
def statement_printer(min_diameter, tens):
    #Prints the required information, involving the inputted data
    print("\tThe following calculations have been made for users with the following parameters")
    print(("\tBody Weight: %s kg\t\tCanal Diameter: %s mm\t\tZercanium tensile Strength %s MPa " % (round((var.body_weight / 9.8), 2), var.canal_diameter, var.ultTen_strength)))
    print(("\tThe minimum diameter that can be used for this implant is %s mm" % (round(min_diameter, 2))))
    print(("\tThe applied tensile strength for this implant is %s MPa" % (round(tens, 2))))

