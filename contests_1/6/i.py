N = int(input())

n = [input().split() for i in range(N)]

for k in range(N):
    for j in range(N-k-1):
        if n[j][2] > n[j+1][2]:
            n[j], n[j+1] = n[j+1], n[j]

n1 = []

for i in range(N):
    n1.append(n[i])
    if n[i][1] == 'January':
        n1[i][1] = 1
    elif n[i][1] == 'February':
        n1[i][1] = 2
    elif n[i][1] == 'March':
        n1[i][1] = 3
    elif n[i][1] == 'April':
        n1[i][1] = 4
    elif n[i][1] == 'May':
        n1[i][1] = 5
    elif n[i][1] == 'June':
        n1[i][1] = 6
    elif n[i][1] == 'July':
        n1[i][1] = 7
    elif n[i][1] == 'August':
        n1[i][1] = 8
    elif n[i][1] == 'September':
        n1[i][1] = 9
    elif n[i][1] == 'October':
        n1[i][1] = 10
    elif n[i][1] == 'November':
        n1[i][1] = 11
    elif n[i][1] == 'December':
        n1[i][1] = 12

for k in range(N):
    for j in range(N-k-1):
        if n1[j][1] > n1[j+1][1] and n1[j][2] == n1[j+1][2]:
            n1[j], n1[j+1] = n1[j+1], n1[j]

for i in range(N):
    if n1[i][1] == 1:
        n1[i][1] = 'January'
    elif n1[i][1] == 2:
        n1[i][1] = 'February'
    elif n1[i][1] == 3:
        n1[i][1] = 'March'
    elif n1[i][1] == 4:
        n1[i][1] = 'April'
    elif n1[i][1] == 5:
        n1[i][1] = 'May'
    elif n1[i][1] == 6:
        n1[i][1] = 'June'
    elif n1[i][1] == 7:
        n1[i][1] = 'July'
    elif n1[i][1] == 8:
        n1[i][1] = 'August'
    elif n1[i][1] == 9:
        n1[i][1] = 'September'
    elif n1[i][1] == 10:
        n1[i][1] = 'October'
    elif n1[i][1] == 11:
        n1[i][1] = 'November'
    elif n1[i][1] == 12:
        n1[i][1] = 'December'

for k in range(N):
    for j in range(N-k-1):
        if int(n1[j][0]) > int(n1[j+1][0]) and n1[j][2] == n1[j+1][2] and n1[j][1] == n1[j+1][1]:
            n1[j], n1[j+1] = n1[j+1], n1[j]

for k in range(N):
    for j in range(N-k-1):
        hours_1 = n1[j][3].split(':')[0]
        minutes_1 = n1[j][3].split(':')[1]
        hours_2 = n1[j+1][3].split(':')[0]
        minutes_2 = n1[j+1][3].split(':')[1]
        if (int(hours_1) > int(hours_2) or (int(hours_1) == int(hours_2) and int(minutes_1) > int(minutes_2))) and n1[j][2] == n1[j+1][2] and n1[j][1] == n1[j+1][1] and n1[j][0] == n1[j+1][0]:
            n1[j], n1[j+1] = n1[j+1], n1[j]

for i in range(len(n1)):
    print(*n1[i])