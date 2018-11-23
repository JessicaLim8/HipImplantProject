import math
import var

#calculates the stress amplitude
def stress_amp(dia):
    area = math.pi * ((dia / 2) ** 2)
    fail  = (10 * var.body_weight) / area
    return fail

#calculates the number of required cycles    
def cycle_calc(stress_fail):
    current_stress = stress_fail
    cycles = -1
    data = []
    data = read_data("metaldata.txt") 
    #loops through the values of the file until the stress_fail is bigger than the stress-strain curve        
    for lines in data:
        cycles = cycles + 1
        #breaks if value is above curve
        if lines[1] < current_stress: 
            break
        #continues if value is below the curve    
        else:
            current_stress = current_stress * (6 + math.log10(cycles) ** (14 / 30)) 
    return cycles

#read the file            
def read_data(filename):
    in_file = open(filename,"r")
    lines_list = []
    #call the readlines function
    lines_list = read_lines(in_file)
    in_file.close()
    file_list = []
    #iterate through the list of strings from the file
    for line in lines_list:
        split_str = line.split()
        split_float = []
        #convert each string into a float
        for var in split_str:
            split_float.append(float(var))
        #add the float list to the file list of floats
        file_list.append(split_float)
    return file_list

#read all the lines
def read_lines(filename):
    all_lines = []
    #read all the lines and add to list
    for x in filename:
        all_lines.append(x)
    return all_lines
    
    #main function, calls other functions and prints the calculated values
def return_calculations(dia):
    stress_fail = stress_amp(dia)
    cycles_fail = cycle_calc(stress_fail)
    #prints calculated values
    #print("The implant will fail after %s cycles" % (cycles_fail))
    #print("The maximum stress amplitude that corresponds to failture is ", stress_fail)
    return stress_fail, cycles_fail
