#%%
# AUTHOR:     Trent Brunson
# COURSE:     ANLY 615
# PROGRAM:    Triathlon fuel comsumption
# PURPOSE:    This will return how many calories are burned (& weight lost) for a trio of execerises. 
# INPUT:      Times for each of 3 activities: swim, bike & run.
# PROCESS:    Use given values for caloric burn per activity.
# OUTPUT:     How many minutes to achieve the desired temp.
# HONOR CODE: On my honor, as an Aggie, I have neither given 
#             nor received unauthorized aid on this academic work.

# setting values

choice = "Y"

print("*********************************************************************************\n"
    "This program calculates how many calories you burned performing triathlon events.\n" + 
    "*********************************************************************************\n\n")

while choice.upper() == "Y":
    swimTime = int(input("How long did you swim? (minutes)\t"))
    bikeTime = int(input("How long did you bike? (minutes)\t"))
    runningTime = int(input("How long did you run? (minutes)\t\t"))
    
    totalCalBurn = ((swimTime * 275 / 60) + (bikeTime * 200 / 60) + (runningTime * 475 / 60))
    weightLost = totalCalBurn / 3500

    print(f"Your burned {int(round(totalCalBurn)):} calories and lost {weightLost:.2f} pounds.\n\n")

    choice = input("Would you like to enter another workout/event? (Y/N)")
# %%
