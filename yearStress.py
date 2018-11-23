import math
import var

areaBone = (math.pi * (var.canalDiameter/2)**2)
ERatio = math.sqrt((var.modulusImplant/var.modulusBone))

def failureCalc():
    #This program calculate the number of years before the femur will fracture
    years = 1
    compStress = ((30 * var.bodyWeight)/ areaBone) #Stress from an axial load
    compStrength = program3_compStrength(years) #Defines strength of the bone based on years since implant
    stressReduc = compStress * ((2 * var.modulusBone)/(var.modulusBone + var.modulusImplant)) **(1/2)
    #condition for possible femur fracture
    while stressReduc <= compStrength:
        compStress = ((30 * var.bodyWeight)/ areaBone)
        compStrength = program3_compStrength(years)
        stressReduc = compStress * ((2 * var.modulusBone)/(var.modulusBone + var.modulusImplant)) **(1/2)
        years += 1
    years -= 1
    yrsFail = years
    print("\tYour implant will fail in approximately", yrsFail, "years.") #Returns number of years until failure
    stressFail = program3_compStrength(yrsFail) #Calculates stress associated with fracture
    print("\tThe compressive stress will be equal to:", (-1 *(round(stressFail, 2))), " MPa when the femur fractures.")

def program3_compStrength(years):
    compStrength = ((0.001 * (years ** 2)) - (3.437 * years * ERatio) + 181.72)
    return compStrength
