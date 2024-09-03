def add_time(start, duration, weekday=''):
    # Splitting the input time and duration
    start_time, start_type = start.split(" ")
    start_hrs, start_mins = map(int, start_time.split(":"))
    duration_hrs, duration_mins = map(int, duration.split(':'))

    # Corrected days of the week
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    # Convert PM to 24-hour format
    if start_type == 'PM':
        start_hrs += 12

    # Calculate new minutes and additional hours
    new_mins = (start_mins + duration_mins) % 60
    add_hrs = (start_mins + duration_mins) // 60

    # Calculate new hours and additional days
    new_hrs = (start_hrs + duration_hrs + add_hrs) % 24
    add_day = (start_hrs + duration_hrs + add_hrs) // 24

    # Determine AM/PM and adjust hours
    if new_hrs >= 12:
        new_type = 'PM'
        if new_hrs > 12:
            new_hrs -= 12
    else:
        new_type = 'AM'
        if new_hrs == 0:
            new_hrs = 12

    # Calculate new weekday if provided
    if weekday:
        weekday = weekday.capitalize()
        index = day.index(weekday)
        display_index = (index + add_day) % len(day)
        display_day = day[display_index]
    else:
        display_day = ''

    # Form the result string
    if add_day == 0:
        if weekday:
            new_items = f"{new_hrs}:{new_mins:02} {new_type}, {display_day}"
        else:
            new_items = f"{new_hrs}:{new_mins:02} {new_type}"
    elif add_day == 1:
        if weekday:
            new_items = f"{new_hrs}:{new_mins:02} {new_type}, {display_day} (next day)"
        else:
            new_items = f"{new_hrs}:{new_mins:02} {new_type} (next day)"
    else:
        if weekday:
            new_items = f"{new_hrs}:{new_mins:02} {new_type}, {display_day} ({add_day} days later)"
        else:
            new_items = f"{new_hrs}:{new_mins:02} {new_type} ({add_day} days later)"

    return new_items




