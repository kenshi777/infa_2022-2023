s = input()
st_r = ''
count = 0
for i in s:
    if i.isalpha():
        if count == 0:
            st_r += i.upper()
        else:
            st_r += i.lower()

        count += 1
        count %= 2
    else:
        st_r += i

print(st_r)



