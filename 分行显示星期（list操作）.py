week=['Mon.', 'Tues.', 'Wedn.', 'Thur.', 'Fri.']
weekend=['Sat.', 'Sun.']
#week.append(weekend)
week.extend(weekend)
for i, j in enumerate(week, 1):
    print(i, j)

for element in week:
    print(element)

