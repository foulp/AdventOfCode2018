import pathlib


def init_orders(steps):
    before = [step[1] for step in steps]
    after = [step[7] for step in steps]
    steps = list(zip(before, after))
    return before, after, steps


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        steps_input = [order.split() for order in f.read().split('\n')]

    before, after, steps = init_orders(steps_input)

    letters = sorted(set(step[0] for step in steps).union(set(step[1] for step in steps)))

    # Part One
    done = []
    for _ in range(len(letters)):
        new = next(let for let in letters if let not in after+done)
        steps = [t for t in steps if t[0] != new]
        before = [t[0] for t in steps]
        after = [t[1] for t in steps]
        done.append(new)

    print(f"The result of first star is {''.join(done)}")

    # Part Two
    before, after, steps = init_orders(steps_input)

    workers = 5
    steps_duration = 60
    clock = 0
    done = []
    doing = {}
    for i in sorted(set([bef for bef in letters if bef not in after+done])):
        doing.update({i: len(doing)})
        if len(doing) == workers:
            break

    time_started = {a: 0 for a in doing.keys()}
    while len(done) < len(letters):
        clock += 1
        ended = [action for action in doing.keys() if clock-time_started[action] == steps_duration+sorted(letters).index(action)+1]
        done += sorted(ended)
        free = [w for w in range(workers) if w not in doing.values()]
        for action in ended:
            del time_started[action]
            free.append(doing[action])
            del doing[action]

        steps = [t for t in steps if t[0] not in ended]
        before = [t[0] for t in steps]
        after = [t[1] for t in steps]
        to_be_started = sorted([l for l in letters if l not in done + after + list(doing.keys())])
        for a in to_be_started:
            if len(free):
                doing[a] = free[0]
                time_started[a] = clock
                free = free[1:]

    print(f"The result of second star is {clock}")
