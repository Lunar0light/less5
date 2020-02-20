data_x = [1]
i_cons=[]
f = open('task5.txt', 'w')
data_x = input('Input integer num: ')
f.write(data_x)
f.close()
fu = open("task5.txt")
cons = fu.readlines()
#print(cons)
cons=str(cons)
#print(cons)
cons=cons[2:-2]
#print(cons)
cons=cons.split(' ')
#print(cons)
for i in range(0, len(cons)):
    i_cons.append(int(cons[i]))
print('Sum=',sum(i_cons))

