import os
import math

#teamNumber = 14
bodyWeight = 3
#outerDia = 6
canalDiameter = 7
canalOffset = 8
#modulusBone = 9
ultTenStrength = 45
#modulusImplant = 3
stemDia = 5
width = os.get_terminal_size().columns

#calculates the stress amplitude
def stressAmp(dia):
    area = math.pi * ((dia / 2) ** 2)
    fail  = (10 * bodyWeight) / area
    return fail

#calculates the number of required cycles    
def cycleCalc(stressFail):
    currentStress = stressFail
    cycles = -1
    data = []
    data = read_data("metaldata.txt") 
    k = 6 + (math.log(10) ** (14/30))
    #loops through the values of the file until the stressFail is bigger than the stress-strain curve        
    for lines in data:
        cycles = cycles + 1
        #breaks if value is above curve
        if lines[1] < currentStress: 
            break
        #continues if value is below the curve    
        else:
            currentStress = currentStress * k
    return cycles

#read the file            
def read_data(filename):
    in_file = open(filename,"r")
    lines_list = []
    #call the readlines function
    lines_list = readlines(in_file)
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
def readlines(filename):
    all_lines = []
    #read all the lines and add to list
    for x in filename:
        all_lines.append(x)
    return all_lines
    
    #main function, calls other functions and prints the calculated values
def sub2():
    stressFail = stressAmp(dia)
    cyclesFail = cycleCalc(stressFail)
    #prints calculated values
    print("The implant will fail after %s cycles" % (cyclesFail))
    print("The maximum stress amplitude that corresponds to failture is ", stressFail)

sub2()
