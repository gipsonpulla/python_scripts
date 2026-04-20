#print tables of a number

def print_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    print_table(5)