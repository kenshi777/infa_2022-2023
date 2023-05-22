n = int(input())
cubes = [i * i * i for i in range(0, 100)]
 
def find_cubes(n):
    for i, a in enumerate(cubes):
        for j, b in enumerate(cubes):
            if a + b == n:
                return i, j
 
res = find_cubes(n)
print(*res) if res else print('impossible')