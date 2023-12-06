input = ["Time:        44     82     69     81",
"Distance:   202   1076   1138   1458"]
race_time = int(input[0].split(":")[1].strip().replace(" ",""))
record_distance = int(input[1].split(":")[1].strip().replace(" ",""))
records = []
charge_up_range = range(0, race_time)
new_records = 0
for charge in charge_up_range:
    speed = charge
    distance_travelled_remaining = speed * (race_time - charge)
    if(distance_travelled_remaining > record_distance):
        new_records += 1
records.append(new_records)

print(records)