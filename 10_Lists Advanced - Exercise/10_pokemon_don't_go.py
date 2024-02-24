pokemons = [int(num) for num in input().split()]
catched_pokemons = 0
while True:
    if len(pokemons) == 0 or pokemons == []:
        break
    index = int(input())
    if index < 0:
        catched_pokemons += pokemons[0]
        removed = pokemons[0]
        pokemons[0] = pokemons[-1]
        for current_pokemeon in pokemons:
            if current_pokemeon <= removed:
                pokemons[pokemons.index(current_pokemeon)] += removed
            else:
                pokemons[pokemons.index(current_pokemeon)] -= removed

    elif index >= len(pokemons):
        catched_pokemons += pokemons[-1]
        removed = pokemons[-1]
        pokemons[-1] = pokemons[0]
        for current_pokemeon in pokemons:
            if current_pokemeon <= removed:
                pokemons[pokemons.index(current_pokemeon)] += removed
            else:
                pokemons[pokemons.index(current_pokemeon)] -= removed

    else:
        element = pokemons[index]
        catched_pokemons += element
        pokemons.remove(element)
        for current_pokemeon in pokemons:
            if current_pokemeon <= element:
                pokemons[pokemons.index(current_pokemeon)] += element
            else:
                pokemons[pokemons.index(current_pokemeon)] -= element

print(abs(catched_pokemons))
