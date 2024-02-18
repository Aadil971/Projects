# ENDG 233 Fall 2023
# Portfolio Project 1
# rover.py
# Program for calculating the time it takes a rover_selection to travel depending on rover parameters and storm status.
# Aadil Bashir


# This module can be used to access math.floor() and math.ceil() as needed.
# e.g. math.floor(10/3) = 3, math.ceil(10/3) = 4
import math


rover_selection=int(input('Which rover would you like to move?'))
distance = float(input('How far is the mission in km?'))
storm = input("Is there a storm in the forecast (True or False)?")

   
     
if rover_selection==1:
    battery=100        #battery in kWh, 
    efficiency=50      #efficiency in kWh/100km, 
    solar_capacity=5   #solar_capacity in kW 
    velocity=5     #velocity in kW
    cycle_distance=(battery/efficiency)*100    #cycle_distance is how far a rover can travel before it runs out of battery. In km
    cycle_hour=cycle_distance/velocity           #Time taken to use up the battery power
    battery_time=battery/solar_capacity         #Time taken to charge
    if 0 < distance<=cycle_distance:                 #To find out if the rover can complete the travel before running out of battery
        if storm=="True":
            total_time=1.2*(distance/velocity)
        else:
            total_time=distance/velocity
    elif distance>cycle_distance:
        count = distance/cycle_distance            #The count variable is present to find how many cycles of movement and recharge the rover has to go through.
        count= math.floor(count)                 #By rounding down count, we can find the number of cycles, and 
        remianing_distance=distance-(cycle_distance*count)       #the rest of the distance the rover has to travel.
        total_time=(cycle_hour*count)+(battery_time*count)+(remianing_distance/velocity)
        if storm=="True":
            total_time=1.2*total_time
    print("The total travel time for rover{0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_selection, distance, total_time))
elif rover_selection==2:
    battery=130
    efficiency=40
    solar_capacity=8
    velocity=4
    cycle_distance=(battery/efficiency)*100 
    cycle_hour=cycle_distance/velocity
    battery_time=battery/solar_capacity 
    if distance<=cycle_distance:                     #The 2nd rover can travel 325km before needing to charge
        total_time = distance/velocity
        if storm=="True":
            total_time=1.2*total_time
    elif distance>cycle_distance:
        count = distance/cycle_distance
        count= math.floor(count)
        remianing_distance=distance-(cycle_distance*count)
        total_time=(cycle_hour*count)+(battery_time*count)+(remianing_distance/velocity)
        if storm=="True":
            total_time=1.2*total_time
    print("The total travel time for rover{0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_selection, distance, total_time))
elif rover_selection==3:
    battery=80
    efficiency=30
    solar_capacity=4
    velocity=6
    cycle_distance=(battery/efficiency)*100 
    cycle_hour=cycle_distance/velocity
    battery_time=battery/solar_capacity 
    if distance<=cycle_distance:               #The 3rd rover can travel 800/3km before needing to charge
        total_time = distance/velocity
        if storm=="True":
            total_time=1.2*total_time
    elif distance>cycle_distance:
        count = distance/cycle_distance
        count=math.floor(count)
        remianing_distance=distance-(cycle_distance*count)
        total_time=(cycle_hour*count)+(battery_time*count)+(remianing_distance/velocity)
        if storm=="True":
            total_time=1.2*total_time
    print("The total travel time for rover{0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_selection, distance, total_time))
else:
    print("Rover number not recognized.")





