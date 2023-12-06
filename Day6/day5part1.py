import math
input = ["Time:        44     82     69     81",
"Distance:   202   1076   1138   1458"]

race_time = list(map(int,input[0].split(":")[1].strip().split()))
record_distance = list(map(int,input[1].split(":")[1].strip().split()))
race_and_record = [(race_time[i],record_distance[i]) for i in range(len(race_time))]
records = []
for time,record in race_and_record:
    charge_up_range = range(0, time)
    new_records = 0
    for charge in charge_up_range:
        speed = charge
        distance_travelled_remaining = speed * (time - charge)
        if(distance_travelled_remaining > record):
            new_records += 1
    records.append(new_records)
print(math.prod(records))