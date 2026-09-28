def index_of_min(values):
    if (len(values) == 0):
        print(-1)
    else:
        for i in range(len(values)):
            if values[i] == min(values):
                print(i)
                break
if __name__ == "__main__":
    index_of_min([10, -3, -5, 2, 5])   # 2
    index_of_min([1, 2, 3])            # 0
    index_of_min([4, 1, 1, 9])         # 1
    index_of_min([])                   # -1