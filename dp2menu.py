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
            sub_choice = int(input("Select the subprogram you would like to run: "))
            break
        except ValueError:
            print(f"You have entered an invalid input, please try again.\n\t If you would like to see the menu again, press 0 ")
    return sub_choice

#Menu Selection Function:
def menu_func():
    x = 0
    while x == 0:
        #Accounts for user error in entering their subprogram choice
        sub_choice = error_func()
        if sub_choice == 1:
            diameter = diameterCalc.minDiamCalc()
            diameterCalc.statementPrinter(diameter)
        elif sub_choice == 2:
            diameter = diameterCalc.minDiamCalc()
            amp, cycles = stresslifeCalc.returnCalculations(diameter)
            print("\t The implant will fail after %s cycles" % (cycles))
            print("\t The maximum stress amplitude that corresponds to failture is ", amp)
        elif sub_choice == 3:
            yearStress.failureCalc()
        elif sub_choice == 4:
            print("Thank you for using our stress analysis program, goodbye.")
            break
        elif sub_choice == 0:
            main_menu()
        else:
            print(f"Sorry, this program does not exist.\n\t If you would like to see the menu again, press 0")

main_menu()
menu_func()
