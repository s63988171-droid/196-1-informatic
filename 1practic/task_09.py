def max_of_three(a, b, c):
    if (a>=b and a>=c):
        return(a)
    elif (b>=a and b>=c):
        return(b)
    elif (c>=b and c>=a):
        return(c)

if __name__ == "__main__":
    max_of_three(1, 2, 3)     # 3
    max_of_three(10, 2, 3)    # 10
    max_of_three(1, 1, 1)     # 1
    max_of_three(-5, -2, -9)  # -2