from util import Stack, Queue

cache = {}

def earliest_ancestor(ancestors, starting_node):
    for i in ancestors:
        if i[0] not in cache:
            cache[i[0]] = set()
            cache[i[0]].add(i[1])

        else:
            cache[i[0]].add(i[1])

    s = Stack()

    visited = set()
    array_list = list()

    s.push([starting_node])

    while s.size():
        path = s.pop()
        array_list.append(path)

        v = path[-1]

        if v not in visited:
            visited.add(v)

            for next_vert in get_ancestors(v):
                new_path = list(path)
                new_path.append(next_vert)
                s.push(new_path)

    biggest_index = (0, 0)
    for index, item in enumerate(array_list):
        if len(item) > biggest_index[1]:
            biggest_index = (index, len(item))
        elif len(item) == biggest_index[1]:
            if item[-1] < array_list[biggest_index[0]][-1]:
                biggest_index = (index, len(item))

    if len(array_list) > 1:
        return array_list[biggest_index[0]][-1]
    else:
        return -1

def get_ancestors(v):
    parents = list()

    for key, value in cache.items():
        for second_value in value:
            if v == second_value:
                parents.append(key)

    return parents
