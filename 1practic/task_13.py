def multiplication_table(n):
    table=[]
    for i in range(1,10):
       table.append(f"{n} x {i} = {n * i}") 
    return(table)
if __name__ == "__main__":
    multiplication_table(7)
    multiplication_table(5)