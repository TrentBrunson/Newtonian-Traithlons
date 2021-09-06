#%%
# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Newtonian rate of cooling
# PURPOSE:    This will return how long takes for a liquid to cool to the desired temp. 
# INPUT:      room temperature, current liquid temperature, and desired liquid temperature.
# PROCESS:    The program plugs and chugs the proportinal rate of change.
# OUTPUT:     How many minutes to achieve the desired temp.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# setting values
k = 0.079 #cooling rate coefficient
choice = "Y"

print("*******************************************************************************\n"
    "This program calculates and displays how long it takes a liquid to cool to your\n"
    "desired temperature based on the liquid's starting temperature and the current\n" 
    "room temperature.\n" + 
    "*******************************************************************************\n\n")

while choice.upper() == "Y":

    timer = 1 # init timer

    try:
        roomTemp = float(input("What is the current room temperature?\t\t"))
        liquidTemp = float(input("What is the current temperature of your liquid?\t"))
        desiredTemp = float(input("At what temperature would you like your liquid?\t"))

        if desiredTemp > roomTemp and desiredTemp > liquidTemp:
            print("Please heat your drink in the microwave.\n\n")
            choice = "N" 
        elif desiredTemp < roomTemp and desiredTemp < liquidTemp:
            print("Please put your drink in the fridge.\n\n")
            choice = "N"
        elif desiredTemp > liquidTemp and desiredTemp < roomTemp:
            while liquidTemp < desiredTemp:
                liquidTemp -= (liquidTemp - roomTemp) * k
                timer += 1
            print(f"Your drink will reach {liquidTemp:.2f} degrees after {timer} minutes./n")
        else:
            while liquidTemp > desiredTemp:
                liquidTemp -= (liquidTemp - roomTemp) * k
                timer += 1
            print(f"Your drink will reach {liquidTemp:.2f} degrees after {timer} minutes./n")

        choice = input("Would you like to try again? (Y/N) ")    

    except ValueError:
        print("Input only numbers.")
        choice = "N" 