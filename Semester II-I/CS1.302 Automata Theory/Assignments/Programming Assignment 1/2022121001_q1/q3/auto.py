list = [[3, 3], [7, 3], [11, 3], [15, 3], [3, 7], [7, 7], [11, 7], [15, 7], [3, 11], [7, 11], [11, 11], [15, 11]]

file = open("config.txt", "w")
# for each m n in list, write: m n+1, m+1 n, m-1 n, m n-1, m+1 n+1, m-1 n-1, m-1 n+1, m+1 n-1 in file as integers
file.write("{} {} 96\n".format(16, 13))
for each in list:
    m = each[0]
    n = each[1]
    file.write(str(m) + " " + str(n+1) + "\n")
    file.write(str(m+1) + " " + str(n) + "\n")
    file.write(str(m-1) + " " + str(n) + "\n")
    file.write(str(m) + " " + str(n-1) + "\n")
    file.write(str(m+1) + " " + str(n+1) + "\n")
    file.write(str(m-1) + " " + str(n-1) + "\n")
    file.write(str(m-1) + " " + str(n+1) + "\n")
    file.write(str(m+1) + " " + str(n-1) + "\n")
file.close()