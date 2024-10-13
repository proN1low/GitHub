from datetime import datetime

print("Kérem adja meg az első időpontot:")
a_hour = int(input("Óra: "))
a_min = int(input("Perc: "))
a_sec = int(input("Másodperc: "))
first_time = str(f'{a_hour}:{a_min}:{a_sec}')
print(f'Az első időpont: {first_time}')

print("Kérem adja meg a második időpontot:")
b_hour = int(input("Óra: "))
b_min = int(input("Perc: "))
b_sec = int(input("Másodperc: "))
second_time = str(f'{b_hour}:{b_min}:{b_sec}')
print(f'A második időpont: {second_time}')

time_format = "%H:%M:%S"
start = datetime.strptime(first_time, time_format)
end = datetime.strptime(second_time, time_format)
difference = end-start
seconds = int(difference.total_seconds())
print(f'A különbség másodpercben: {seconds}')
