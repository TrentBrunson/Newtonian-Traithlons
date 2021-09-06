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

print("*****************************************************************************\n"
    "This program calculates and displays it takes a liquid to cool to your desired temperature\n" + 
    "based on the liquid's starting temperature and current room temperature.\n" + 
    "*******************************************************************************\n\n")

while choice.upper() == "Y":
    roomTemp = input("What is the current room temperature?\t\t")
    liquidTemp = input("What is the current temperature of your liquid?\t")
    desiredTemp = input("At what temperature would you lik your liquid?")

    