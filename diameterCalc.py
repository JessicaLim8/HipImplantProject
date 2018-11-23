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
    function = equation[0] * (min_diameter ** 3) - equation[1] * (min_diameter ** 2) - equation[2]
    deriviative = equation[0] * 3  * (min_diameter ** 2) - equation[1] * 2 * min_diameter
    # evaluates x1 = x0 - f(x) / f'(x)
    min_diameter = min_diameter - (function / deriviative)
    return min_diameter

#calculates the value of the value of the function with the newly calculated minimum diameter
def check(equation, min_diameter):
    zero = equation[0] * (min_diameter ** 3) - equation[1] * (min_diameter ** 2) - equation[2]
    return zero

#main program that calls other functions 
def minDiam_calc():
    #calls other functions to make calculations
    appTen_stress = var.body_weight * 3.5
    a = axial(appTen_stress)
    b  = bend(appTen_stress)
    equation = [var.ultTen_stength, a, b]
    minDia = calculate(equation)
    return minDia, (a + b)

#calls sub1 and prints the required information
def statement_printer(min_diameter, tens):
    #Prints the required information, involving the inputted data
    print("\tThe following calculations have been made for users with the following parameters")
    print("\tBody Weight: ", (var.body_weight / 9.8), "kg")
    print("\tCanal diameter: ", var.canal_diameter, "mm") 
    print("\tZercanium with a tensile strength:  ", var.ultTen_stength, "MPa")
    print(("\tThe minimum diameter that can be used for this implant is %s mm" % (min_diameter)))
    print(("\tThe applied tensile strength for this implant is %s MPa" % (tens)))
