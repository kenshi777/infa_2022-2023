def get_key(x):  # функция, возвращающая второй элемент tuple
    return x[2]


def make_set(x):  # функция для создания множества с вершиной x
    return {
        "parent": x,  # предок вершины - сама вершина 
        "rank": 0  # ранг множества - 0 (сортировка по глубине)
    }


def find_set(x):  # функция поиска множества по вершине
    if dsu[x]["parent"] == x:  # если предок вершины - вершина, то 
        return x               # множество состоит из нее
    dsu[x]["parent"] = find_set(dsu[x]["parent"])
    return dsu[x]["parent"]  # иначе рекуррентно продолжаем поиск


def union_sets(x, y):  # функция для объединения множеств
    x = find_set(x)  # множества, к которым принадлежат вершины
    y = find_set(y)
    if x != y:  # интересен только случай различных вершин
        if dsu[x]["rank"] < dsu[y]["rank"]:  # если ранг множества
            x, y = y, x  # вершины мешьше, то меняем их местами
        dsu[y]["parent"] = x  # объединяем множества соответственно рангу
        if dsu[x]["rank"] == dsu[y]["rank"]:  # если ранг одинаковый,
            dsu[x]["rank"] += 1  # то увеличиваем глубину на 1 у предка


if __name__ == "__main__":
    n, m = map(int, input().split())  # считывание графа
    a = []                            # в виде списка ребер
    for i in range(m):
        u, v, w = map(int, input().split())
        a.append((u, v, w))
    a.sort(key=get_key)  # сортируем ребра по весу
    dsu = [make_set(i) for i in range(n)]  # создаем n множеств
    edges = []  # список ребр минимального остова
    weight = 0  # его вес
    for u, v, w in a:  # для всех ребер проверяем, что соседние
        if find_set(u) != find_set(v):  # вершины принадлежат одному множеству
            weight += w  # если нет, то добавляем вершину в множество
            edges.append(str(u) + ' ' + str(v))
            union_sets(u, v)  # и обновляем список ребер остова и его вес
    print(weight)
    print(*edges, sep="\n")