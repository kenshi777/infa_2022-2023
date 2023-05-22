def find(s, s1):
    ind = []
    for i in range(len(s)-len(s1)+1):
        if s[i:i + len(s1)] == s1:
            ind.append(i)
    return ind

print(find('aabbbvvv', 'bbv'))