    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
    else:
        overtime = totalHours - 40
        regularHours = 40
    return hourlyWage*regularHours + (1.5*hourlyWage)*overtime
