import math
import var

area_bone = (math.pi * (var.canal_diameter/2)**2)
e_ratio = math.sqrt((var.modulus_implant/var.modulus_bone))

def failure_calc():
    #This program calculate the number of years before the femur will fracture
    years = 1
    comp_stress = ((30 * var.body_weight)/ area_bone) #Stress from an axial load
    comp_strength = program3_comp_strength(years) #Defines strength of the bone based on years since implant
    stress_reduc = comp_stress * ((2 * var.modulus_bone)/(var.modulus_bone + var.modulus_implant)) **(1/2)
    #condition for possible femur fracture
    while stress_reduc <= comp_strength:
        comp_stress = ((30 * var.body_weight)/ area_bone)
        comp_strength = program3_comp_strength(years)
        stress_reduc = comp_stress * ((2 * var.modulus_bone)/(var.modulus_bone + var.modulus_implant)) **(1/2)
        years += 1
    years -= 1
    yrs_fail = years
    print("\tYour implant will fail in approximately", yrs_fail, "years.") #Returns number of years until failure
    stressFail = program3_comp_strength(yrs_fail) #Calculates stress associated with fracture
    print("\tThe compressive stress will be equal to:", round(stressFail, 2)," MPa when the femur fractures.")

def program3_comp_strength(years):
    comp_strength = ((0.001 * (years ** 2)) - (3.437 * years * e_ratio) + 181.72)
    return comp_strength
