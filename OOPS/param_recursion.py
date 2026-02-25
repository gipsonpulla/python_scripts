def sum_numbers(sum, i , N):
    if i > N:
        print (sum)
        return
    sum_numbers(sum+i, i+1, N)

sum_numbers(0, 1, 5)    