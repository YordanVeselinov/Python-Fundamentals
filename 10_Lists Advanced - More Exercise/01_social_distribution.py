def distribute_wealth(population_str, min_wealth):
    population = list(map(int, population_str.split(', ')))
    while True:
        max_wealth = max(population)
        min_wealth_present = min(population)
        wealth_diff = max_wealth - min_wealth_present
        if wealth_diff < min_wealth:
            print(f"[{', '.join(map(str, population))}]")
            print(min_wealth_present)
            print("No equal distribution possible")
            break
        else:
            population[population.index(max_wealth)] -= min_wealth
            population[population.index(min_wealth_present)] += min_wealth
            if min(population) >= min_wealth:
                print(f"[{', '.join(map(str, population))}]")
                break


population_input = input().strip()
min_wealth_input = int(input().strip())


distribute_wealth(population_input, min_wealth_input)
