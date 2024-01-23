fh = open('Practical-9.txt', 'w')
n = 10
for j in range(1, n):
    for i in range(1, 11):
        fh.write(str(j) + ' X ' + str(i) + ' = ' + str(j * i) + '\n')
    fh.write('-------------------\n')

fh.close()

