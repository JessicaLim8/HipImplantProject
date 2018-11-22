"""
Author: Liam Ward and Jessica Lim
Objective: DP2 Program Menu
"""
import math
#Variables:
teamNumber = 14
bodyWeight = 1
modulusBone = 1
modulusImplant = 1
outerDia = 1 #Outer diameter of stem
canalDiameter = 1#inner diameter of stem
canalOffset = 1 #Canal offset from femoral head
modulusBone = 1 #modulus of elasticity of cortical bone
ultTenStrength = 1 # the ultimate strength of the implant
modulusImplant = 1 # the elastic modulus of the implant
stemDia = 1 #Diameter of the implant stem
#Function to account for user input error:

def main_menu():
    #Home menu setup:
    print("  Program Menu: ")
    print("\t1. Subprogram 1")
    print("\t2. Subprogram 2")
    print("\t3. Subprogram 3")
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
            import dp2sub1
        elif sub_choice == 2:
            dia = "global"
            dia = from dp2sub1 import sub1
            import dp2sub2
        elif sub_choice == 3:
            import dp2sub3
        elif sub_choice == 4:
            print("Thank you for using our stress analysis program, goodbye.")
            break
        elif sub_choice == 0:
            main_menu()
        else:
            print(f"Sorry, this program does not exist.\n\t If you would like to see the menu again, press 0")
def main():
    main_menu()
    menu_func()
main()
