data_x = [1]
f = open('task1.txt', 'w')
while data_x != '':
     data_x = (input('Input data: \n'))
     f.write(data_x)
     f.write('\n')

