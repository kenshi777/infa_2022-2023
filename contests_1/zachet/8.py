a = [1, 2, 3, 14, 23, 25, 41, 40, 14]
m_1 = m_2 = m_3 = float('-inf')

for i in range(len(a)):
    if a[i] >= m_1:
        m_1, m_2, m_3 = a[i], m_1, m_2
    elif a[i] >= m_2:
        m_2, m_3 = a[i], m_2
    elif a[i] >= m_3:
        m_3 = a[i]

print(m_1, m_2, m_3)