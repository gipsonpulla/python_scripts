file_name = input("Enter the file name without extension")
file_name = file_name + ".txt"
with open(file_name, "a") as f:
    while True:
        sentence = input("Enter the sentence")
        if sentence == "q" or sentence == "Q":
            break
        f.write(sentence)
