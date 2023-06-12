def add_time(start_time: str, duration_time: str, starting_day: str = None) -> str:
    """
This function add the duration time to the start time and return the result.
    :param start_time: a start time in the 12-hour clock format (ending in AM or PM)
    :param duration_time: a duration time that indicates the number of hours and minutes
    :param starting_day: (optional) a starting day of the week, case insensitive
    """
    result = []
    ret: str = ""
    # Preparar una lista con cada elemento por separado
    # para poder trabajar con ellos mas comodamente luego
    start_time_list = str(start_time).replace(':', ' ').split()
    # Convertir a formato de 24 horas
    if start_time_list[2] == 'PM':
        start_time_list[0] = str(int(start_time_list[0]) + 12)
    start_time_list.pop(2)
    if starting_day is not None:
        start_time_list.insert(0, str(starting_day))
    else:
        start_time_list.insert(0, '')
    # Now
    # start_time_list[0] -> Day of the week
    # start_time_list[1] -> Hour
    # start_time_list[2] -> Minutes
    duration_time_list = str(duration_time).replace(':', ' ').split()
    # Now
    # duration_time_list[0] -> hours
    # duration_time_list[1] -> minutes
    if (int(duration_time_list[1]) + int(start_time_list[2])) < 60:
        result.append(int(duration_time_list[1]) + int(start_time_list[2]))
    else:
        result.append(int(duration_time_list[1]) + int(start_time_list[2]) - 60)
        start_time_list[1] = str(int(start_time_list[1]) + 1)
    result.append(int(start_time_list[1]) + int(duration_time_list[0]))
    result.append(result[1] % 24)
    result.append(result[1] // 24)
    result.pop(1)
    if result[1] > 12:
        result[1] = result[1] - 12
        result.insert(0, 'PM')
    elif result[1] == 12:
        result.insert(0, 'PM')
    elif result[1] == 0:
        result[1] = 12
        result.insert(0, 'AM')
    else:
        result.insert(0, 'AM')
    days_of_the_week = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
    if starting_day is not None:
        starting_day = str(starting_day).capitalize()
        if (days_of_the_week[starting_day] + result[3]) > 7:
            result.insert(0, list(days_of_the_week.keys())[days_of_the_week[starting_day] + result[3] - 1 - 7])
        else:
            result.insert(0, list(days_of_the_week.keys())[days_of_the_week[starting_day] + result[3] - 1])
    else:
        result.insert(0, "")
    # Now
    # result[0] -> Day
    # result[1] -> AM o PM
    # result[2] -> Minutes
    # result[3] -> Hours
    # result[4] -> n Days
    if result[4] == 0:
       ret = f'{str(result[3])}:{str(result[2]) if (len(str(result[2])) > 1) else (str(0) + str(result[2]))} {result[1]}{str("") if starting_day is None else str(f", {result[0]}")}'
    elif result[4] == 1:
        ret = f'{str(result[3])}:{str(result[2]) if (len(str(result[2])) > 1) else (str(0) + str(result[2]))} {result[1]}{str("") if starting_day is None else str(f", {result[0]}")} {str(f"(next day)")}'
    else:
        ret = f'{str(result[3])}:{str(result[2]) if (len(str(result[2])) > 1) else (str(0) + str(result[2]))} {result[1]}{str("") if starting_day is None else str(f", {result[0]}")} {str(f"({str(result[4])} days later)")}'
    print(ret)
    return ret
