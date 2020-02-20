person=[]
salary=[]
i_salary=[]
ls=[]

f = open('task3.txt')
cons =f.readlines()
n_lines=len(cons)
#print('num lines=', n_lines)

#for i in enumerate(cons):
for i in range(0, n_lines): #Здесь range почему-то обрабатывает все строки
    words = cons[i].split()
    #print(words)
    person.append(words[0])
    salary.append(words[1])
    i_salary.append(int(salary[i]))
    #dicti= {i: words()}
   # print(person)
    #print(i_salary)

for a in range(0, len(i_salary)):
    if i_salary[a] < 20000:
        ls.append(a+1)
#print(ls)
print('Salary below 20000: ')
for b in range(0, len(ls)):
    print(person[b])

print('average salary', sum(i_salary) / len(i_salary))
