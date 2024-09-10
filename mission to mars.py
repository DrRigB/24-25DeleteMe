def launch_sequence():
    print("Starting countdown!")
    print("T minus 10 .... 9....8.....7....6...5..4..3..2..1 LIFT OFF!")

launch_sequence()

def travel_time_to_mars(distance , speed):
    time = distance / speed
   
    if speed < 20000:
        print("Warning You're not going fast enough")
    elif speed > 50000: 
        print("Warning: speed is too fast!" )
    else:
        print("speed is optimal for mars!")
    
    
    
    print("Travel time to mars is", time, "hours")

   

travel_time_to_mars(225000000, 25000)


#travel times to mars
travel_time_to_mars(2250000000, 15000) #too slow
travel_time_to_mars(2250000000, 550000) #too fast
travel_time_to_mars(2250000000, 30000) # Perfect

def mars_mission(distance, speed, fuel, crew_ready):
    time = distance / speed
    if speed < 20000:
        print("Warning: speed is too slow for timely arrival")
    elif speed> 50000:
        print("Warning:Speed is too fast, risk of overshooting Mars!")
    else:
        print("Fuel levels are sufficent.")
    if fuel < 500000:
        print("Warning: Not enough fu; for the journey!")
    else:
        print("Fuel levels are sufficent.")
    if crew_ready:
        print("Crew is ready for the mission")
    else:
        print("Crew is not ready, Mission delayed")
    print("Estimated travel time to Mars:", time, "hours")

mars_mission(2250000000, 25000, 600000, True) #perfect senario
mars_mission(2250000000, 15000, 400000, True) #Slow speed and low fuel mars_mission(2250000000, 30000, 700000, False) #Crew not ready
mars_mission(2250000000, 30000, 700000, False)