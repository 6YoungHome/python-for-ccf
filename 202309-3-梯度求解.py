n, m = map(int, input().split())

formular = input().split()
ops = '*+-'

stack1 = []
stack2 = []

number_dict = {}
part_dict = {}

for i in range(len(formular)):
    if formular[i] not in ops:
        if formular[i][0] == "-" and formular[i][1::].isnumeric():
            stack1.append(formular[i])
            part_dict[formular[i]] = formular[i]
        elif formular[i].isnumeric():
            stack1.append(int(formular[i]))
            part_dict[formular[i]] = formular[i]
        elif formular[i][0] == 'x':
            stack1.append(formular[i])
            part_dict[formular[i]] = formular[i]
        elif formular[i] == '*':
            tmp1 = stack1.pop()
            tmp2 = stack1.pop()
            part_dict[f"{tmp1}*{tmp2}"] = 
            

print("-100".isnumeric())