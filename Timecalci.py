def add_time(start, duration, day_of_week=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    if period == "PM":
        start_hour += 12
    
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    total_minutes %= 60
    
    final_hour = total_hours % 24
    final_period = "AM" if final_hour < 12 else "PM"
    final_hour = final_hour if final_hour % 12 != 0 else 12
    if final_hour > 12:
        final_hour -= 12
    
    days_later = total_hours // 24
    
    new_time = f"{final_hour}:{total_minutes:02d} {final_period}"
    
    if day_of_week:
        day_of_week = day_of_week.capitalize()
        index = (days_of_week.index(day_of_week) + days_later) % 7
        new_time += f", {days_of_week[index]}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time