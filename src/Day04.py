import pathlib

if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        entries = f.read().split('\n')

    entries.sort()

    # Part One
    current = None
    start = None
    sleeps = {}
    for entry in entries:
        if 'Guard' in entry:
            current = int(entry[entry.index('#')+1:].split()[0])
        if 'asleep' in entry:
            start = int(entry[15:17])
        if 'wakes' in entry:
            if current not in sleeps.keys():
                sleeps[current] = [0] * 60
            for minute in range(start, int(entry[15:17])):
                sleeps[current][minute] += 1

    guard = max(sleeps, key=(lambda key: sum(sleeps[key])))
    minute = sleeps[guard].index(max(sleeps[guard]))
    print(f"The guard that sleeps the most is {guard}. He sleeps the most at minute {minute}")
    print(f"The result of first star is {guard * minute}")

    # Part Two
    current = (0, 0, 0)
    for guard in sleeps:
        occurence = max(sleeps[guard])
        if occurence > current[2]:
            current = (guard, sleeps[guard].index(occurence), occurence)
    print(f"The most alsept minute by a guard is minute {current[0]} by guard {current[1]}")
    print(f"The result of second star is {current[0] * current[1]}")
