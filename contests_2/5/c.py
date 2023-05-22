triangle = list(map(int, input().split()))
point = list(map(int, input().split()))
mirror_points = []
for i in range(0, 6, 2):
    mirror_points += [triangle[i] + 2*(point[0] - triangle[i]),triangle[i+1] + 2*(point[1] - triangle[i+1])]

print(*mirror_points)