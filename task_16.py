def month_calendar(start_weekday, days):
    sum = ""
    sum += "   " * start_weekday
    counter = start_weekday

    for i in range(1, days + 1):
        if i < 10:
            sum += f" {i}"
        else: sum += f"{i}"
        counter += 1

        if counter == 7:
            sum = sum.rstrip() + "\n"
            counter = 0
        else:
            sum += " "

    return sum.rstrip()

if __name__ == "__main__":
    print(month_calendar(6, 31))