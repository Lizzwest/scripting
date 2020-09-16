#open a file
lizz_file = open("lizz.txt", "r")
Lines = lizz_file.readlines()
count = 0
# count 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))
# numbers = [1,2,3]
# for i in range(len(numbers)):
#     num = numbers[i]
    # lizz_file.write("{}\n".format(num))
#write to file
# lizz_file.write("\nHello\n")
#close a file
lizz_file.close()
#read a file
# print(lizz_file.read())

adam_file = open("adam.txt", "w")
adam_file.write("AAdam")
adam_file.close()


