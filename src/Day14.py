import pathlib


def next_recipes(scores, first, second):
    scores += str(int(scores[first]) + int(scores[second]))

    first = (first + int(scores[first]) + 1) % len(scores)
    second = (second + int(scores[second]) + 1) % len(scores)
    return scores, first, second


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        n_recipes = int(f.read())

    recipes = '37'
    first_elf = 0
    second_elf = 1

    # Part One
    while len(recipes) < n_recipes+10:
        recipes, first_elf, second_elf = next_recipes(recipes, first_elf, second_elf)

    print(*recipes[n_recipes:n_recipes+10], sep='')

    # Part Two
    sequence = str(n_recipes)
    recipes = '37'
    first_elf = 0
    second_elf = 1
    while sequence not in recipes[-len(sequence)-1:]:
        recipes, first_elf, second_elf = next_recipes(recipes, first_elf, second_elf)

    print(len(recipes) - len(sequence) - 1 + recipes[-len(sequence)-1:].index(sequence))
