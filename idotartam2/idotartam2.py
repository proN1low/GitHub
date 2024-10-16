from datetime import datetime

start = str(input("Kérem adja meg az első időpontot óra:perc:másodperc formátumban: "))
end = str(input("Kérem adja meg a második időpontot óra:perc:másodperc formátumban: "))

time_format = "%H:%M:%S"

time1 = datetime.strptime(start, time_format)
print(f'Első időpont: {time1.time()}')

time2 = datetime.strptime(end, time_format)
print(f'Második időpont: {time2.time()}')

difference = time2 - time1
print(f'A különbség másodpercben: {int(difference.total_seconds())}')
