#используем task1.txt из первого примера, f.readline перескакивает через строку
n_words=0
line=0
f = open('task2.txt')
cons = f.readlines()
n_lines=len(cons)
print('num lines=', n_lines)

#for i in enumerate(cons):
for i in range(0, n_lines):
    words = cons[i].split()
    #print(words)
    print('num words',i+1,'line=', len(words))
