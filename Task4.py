my_dict = {1 : 'Один', 2 : 'Два', 3 : 'Три', 4 : 'Четыре'}
wordss=[]
i_wordss=[]
f = open('task4.txt')
cons =f.readlines()
n_lines=len(cons)
for i in range(0, n_lines):
    words = cons[i].split(' - ')
    wordss.append(words[1])
#print(wordss)

for a in range(0, len(wordss)):
    i_wordss.append(int(wordss[a]))
    #words_s = my_dict{}
print(i_wordss)

fu = open('task4_n.txt', 'w')
for b in range(1, len(i_wordss)+1):
    fu.write(my_dict[b]) #автоматическая кодировка в win-1251 (читаемо)
    fu.write(' - ')
    fu.write(f'{b}')
    fu.write('\n')