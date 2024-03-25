pokemons = [int(x) for x in input().split()]


def pokemon_finder(pokes):
    total_sum = 0
    while pokes:
        index = int(input())
        if index < 0:
            removed_element = pokes.pop(0)
            pokes.insert(0, pokes[-1])
        elif index > len(pokes) - 1:
            removed_element = pokes.pop(-1)
            pokes.append(pokes[0])
        else:
            removed_element = pokes.pop(index)
        pokes = [x + removed_element if x <= removed_element else x - removed_element for x in pokes]
        total_sum += removed_element
    return total_sum


print(pokemon_finder(pokemons))
