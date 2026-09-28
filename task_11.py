def guests_by_seat(seats):
    count = 1
    result = [0] * len(seats)

    # for i in range(len(seats)):
    #     result.append(0)

    for i in seats:
        result[i-1] = count
        count += 1
    return(result)
if __name__ == "__main__":
    guests_by_seat([1, 2, 3, 5, 4])
# [1, 2, 3, 5, 4]
    guests_by_seat([11, 6, 8, 2, 10, 9, 4, 7, 3, 1, 5])
# [10, 4, 9, 7, 11, 2, 8, 3, 6, 5, 1]