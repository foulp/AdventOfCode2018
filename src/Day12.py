import pathlib

if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        puzzle_input = f.read()

    first_line = puzzle_input.split('\n')[0]
    current = first_line[first_line.index(': ')+2:]

    transform = {seq: new for seq, new in [line.split(' => ') for line in puzzle_input.split('\n')[2:]]}

    for step in range(20):
        temp = '.....' + str(current) + '.....'
        for i in range(2, 5):
            pattern = '.'*(7-i)+current[:i-2]
            assert(len(pattern) == 5)
            temp = temp[:i] + transform[pattern] + temp[i+1:]

        for i in range(len(current)):
            if i == 0:
                pattern = '..' + current[:3]
            elif i == 1:
                pattern = '.' + current[:4]
            elif i == len(current)-2:
                pattern = current[-4:] + '.'
            elif i == len(current)-1:
                pattern = current[-3:] + '..'
            else:
                pattern = current[i-2:i+3]

            assert(len(pattern) == 5)
            temp = temp[:i+5] + transform[pattern] + temp[i+6:]

        for i in range(3):
            pattern = current[-(2-i):] + '.'*(3+i)
            if i == 2:
                pattern = '.....'
            assert(len(pattern) == 5)
            temp = temp[:-(5-i)] + transform[pattern] + temp[-(5-i)+1:]

        current = str(temp)

    print(f"The result of first star is {sum(i-20*5 for i in range(len(current)) if current[i] == '#')}")
