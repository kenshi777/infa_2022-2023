def dist(s1, s2, ins_cost, del_cost, replace_cost):
    moves = [[0 for _ in range(len(s1) + 1000)] for _ in range(len(s2) + 1000)]
    moves[0][0] = 0
    for i in range(1, len(s2) + 1):
        moves[0][i] = moves[0][i - 1] + ins_cost
    for i in range(1, len(s1) + 1):
        moves[i][0] = moves[i - 1][0] + del_cost
        for j in range(1, len(s2) + 1):
            if s1[i - 1] != s2[j - 1]:
                moves[i][j] = min(moves[i - 1][j] + del_cost, moves[i][j - 1] + ins_cost, moves[i - 1][j - 1] + replace_cost)
            else:
                moves[i][j] = moves[i - 1][j - 1]
    return moves[len(s1)][len(s2)]



x, y, z = [int(i) for i in input().split()]
s1 = input()
s2 = input()
print(dist(s1, s2, x, y, z))