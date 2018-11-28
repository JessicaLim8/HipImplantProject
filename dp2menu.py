"""
Author: Liam Ward and Jessica Lim
Objective: DP2 Program Menu
"""
import math
import diameterCalc 
import stresslifeCalc 
import yearStress
import var

def main_menu():
    #Home menu setup:
    print("  Program Menu: ")
    print("\t1. Subprogram 1 - Minimum allowable Diameter of Implant")
    print("\t2. Subprogram 2 - Cycle Life of Implant")
    print("\t3. Subprogram 3 - Lifetime before Failure")
    print("\t4. Exit the Program")

#error checking function
def error_func():
    x = 0
    while x == 0:
        #loop through
        try:
            sub_choice = int(input(" Select the subprogram you would like to run: "))
            print("") #add empty line for formatting
            break
        except ValueError:
            print("You have entered an invalid input, please try again.\n\t If you would like to see the menu again, press 0 ")
    return sub_choice

#Menu Selection Function:
def menu_func():
    x = 0
    while x == 0:
        #Accounts for user error in entering their subprogram choice
        sub_choice = error_func()
        if sub_choice not in range(0, 5): 
            print(f"Sorry, this program does not exist.\n\t If you would like to see the menu again, press 0")
            continue
        if sub_choice == 1:
            diameter, app_tens = diameterCalc.minDiam_calc()
            diameterCalc.statement_printer(diameter, app_tens)
        elif sub_choice == 2:
            diameter, app_tens = diameterCalc.minDiam_calc()
            amp, cycles, fails = stresslifeCalc.return_calculations(diameter)
            if fails== False:
                print("\t The implant never fails")
            else:
                print("\t The implant will fail after %s cycles" % (round(cycles, 2)))
                print("\t The maximum stress amplitude that corresponds to failture is ", round(amp, 2))
        elif sub_choice == 3:
            yearStress.failure_calc()
        elif sub_choice == 4:
            print("Thank you for using our stress analysis program, goodbye.")
            break
        elif sub_choice == 0:
            main_menu()
        print("\nWe hope this information was helpful!\n\t If you would like to see the menu again, press 0")

main_menu()
menu_func()
