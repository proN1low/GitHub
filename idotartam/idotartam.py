def feladat_ido():
    from datetime import datetime

    def megfelelo_perc_masodperc():
        sec_min = int(input("Perc: "))
        while True:
            if sec_min < 0 or sec_min > 59:
                sec_min = int(input("Kérjük megfelelő számot adjon meg (0-59): "))
            else:
                return sec_min

    print("Kérem adja meg az első időpontot:")

    a_hour = int(input("Óra: "))
    while True:
        if a_hour < 0 or a_hour > 23:
            a_hour = int(input("Kérjük megfelelő számot adjon meg (0-23): "))
        else:
            break

    a_min = megfelelo_perc_masodperc()
    a_sec = megfelelo_perc_masodperc()

    first_time = str(f'{a_hour}:{a_min}:{a_sec}')
    print(f'Az első időpont: {first_time}')

    print("Kérem adja meg a második időpontot:")

    b_hour = int(input("Óra: "))
    while True:
        if b_hour < 0 or b_hour > 23:
            b_hour = int(input("Kérjük megfelelő számot adjon meg (0-23): "))
        else:
            break

    b_min = megfelelo_perc_masodperc()
    b_sec = megfelelo_perc_masodperc()

    second_time = str(f'{b_hour}:{b_min}:{b_sec}')
    print(f'A második időpont: {second_time}')

    time_format = "%H:%M:%S"
    start = datetime.strptime(first_time, time_format)
    end = datetime.strptime(second_time, time_format)
    difference = end-start
    seconds = int(difference.total_seconds())
    print(f'A különbség másodpercben: {seconds}')

feladat_ido()