from datetime import datetime

print("Kérem adja meg az első időpontot:")
a_hour = int(input("Óra: "))
if a_hour < 0 or a_hour > 23:
    int(input("Kérjük megfelelő számot adjon meg (0-23): "))
a_min = int(input("Perc: "))
if a_min < 0 or a_min > 59:
    int(input("Kérjük megfelelő számot adjon meg (0-59): "))
a_sec = int(input("Másodperc: "))
if a_sec < 0 or a_sec > 59:
    int(input("Kérjük megfelelő számot adjon meg (0-59): "))
first_time = str(f'{a_hour}:{a_min}:{a_sec}')
print(f'Az első időpont: {first_time}')

print("Kérem adja meg a második időpontot:")
b_hour = int(input("Óra: "))
if b_hour < 0 or b_hour > 23:
    int(input("Kérjük megfelelő számot adjon meg (0-23): "))
b_min = int(input("Perc: "))
if b_min < 0 or b_min > 59:
    int(input("Kérjük megfelelő számot adjon meg (0-59): "))
b_sec = int(input("Másodperc: "))
if b_sec < 0 or b_sec > 59:
    int(input("Kérjük megfelelő számot adjon meg (0-59): "))
second_time = str(f'{b_hour}:{b_min}:{b_sec}')
print(f'A második időpont: {second_time}')

time_format = "%H:%M:%S"
start = datetime.strptime(first_time, time_format)
end = datetime.strptime(second_time, time_format)
difference = end-start
seconds = int(difference.total_seconds())
print(f'A különbség másodpercben: {seconds}')