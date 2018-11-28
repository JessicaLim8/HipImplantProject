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
    cycles_num = 0
    if_fails = False 
    data = []
    data = read_data("metaldata.txt") 
    #loops through the values of the file until the stress_fail is bigger than the stress-strain curve        
    #if current_stress > data[0][0]
    if current_stress < (data[0][0]):
        for lines in data:
            # calculates the k constant
            k = 6 + math.log10(lines[1]) ** (14/30)
            #multiplies the stress by the constant    
            current_stress = stress_fail * k
            #breaks if value is above curve
            cycles_num = lines[1]
            if lines[0] < current_stress: 
                if_fails = True
                break
            #continues if value is below the curve    
    return current_stress, cycles_num,  if_fails

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
    init_fail= stress_amp(dia)
    cycles_fail, stress_fail, if_fails = cycle_calc(init_fail)
    return stress_fail, cycles_fail, if_fails
