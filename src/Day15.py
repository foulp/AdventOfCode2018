import collections
import numpy as np
import pathlib

STARTING_HP = 200


class Grid:
    def __init__(self, maze, elf_attack_power=3):
        self.maze = maze
        self.units = {'G': {}, 'E': {}}
        for x, y in zip(*np.where(maze == 'G')):
            self.units['G'][(x, y)] = Goblin(x, y)
        for x, y in zip(*np.where(maze == 'E')):
            self.units['E'][(x, y)] = Elf(x, y, attack_power=elf_attack_power)

    def shortest_path_to_ennemy(self, unit, open_squares):
        start = (unit.x, unit.y)
        queue = collections.deque([[start]])
        seen = {start}
        candidates = []
        while queue:
            path = queue.popleft()
            if len(candidates) and len(path) > len(candidates[0]):
                return min(candidates, key=lambda c: c[-1:]+c[:-1])
            x, y = path[-1]
            if (x, y) in open_squares:
                candidates.append(path)
            for x2, y2 in ((x-1, y), (x, y-1), (x, y + 1), (x+1, y)):
                if 0 <= x2 < self.maze.shape[0] and 0 <= y2 < self.maze.shape[1] and self.maze[x2, y2] in f'.{unit.adv_unit}' and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        return None

    def turn_routine(self):
        units_to_play = list(self.units['G'].values()) + list(self.units['E'].values())
        units_to_play.sort(key=lambda u: (u.x, u.y))
        units_dead = []
        for unit in units_to_play:
            if (unit.x, unit.y) in units_dead:
                continue

            targets = self.units[unit.adv_unit]
            if len(targets) == 0:
                return 0  # No more target, combat ends

            if all(self.maze[x, y] != unit.adv_unit for x, y in ((unit.x-1, unit.y), (unit.x+1, unit.y), (unit.x, unit.y-1), (unit.x, unit.y+1))):
                open_squares = self.identify_open_squares(targets)
                if len(open_squares) == 0:
                    continue
                path = self.shortest_path_to_ennemy(unit, open_squares)
                if path is None:
                    continue
                next_x, next_y = path[1]
                self.maze[unit.x, unit.y] = '.'
                del self.units[unit.type][(unit.x, unit.y)]
                unit.move(next_x, next_y)
                self.maze[unit.x, unit.y] = unit.type
                self.units[unit.type][(unit.x, unit.y)] = unit

            attack = (STARTING_HP+1, -1, -1)
            for x, y in ((unit.x-1, unit.y), (unit.x, unit.y-1), (unit.x, unit.y+1), (unit.x+1, unit.y)):
                if 0 <= x < self.maze.shape[0] and 0 <= y < self.maze.shape[1] and self.maze[x, y] == unit.adv_unit:
                    attack = min(attack, (self.units[unit.adv_unit][x, y].hit_points, x, y))
            if attack[1] > -1:
                self.units[unit.adv_unit][attack[1], attack[2]].get_hit(unit.attack_power)
                if self.units[unit.adv_unit][attack[1], attack[2]].hit_points <= 0:
                    self.maze[attack[1], attack[2]] = '.'
                    del self.units[unit.adv_unit][attack[1], attack[2]]
                    units_dead.append((attack[1], attack[2]))

        return 1

    def combat(self, no_elves_loss=False):
        nb_turns = 0
        starting_elves = len(self.units['E'])
        while len(self.units['E']) * len(self.units['G']):
            nb_turns += self.turn_routine()
            if no_elves_loss and len(self.units['E']) < starting_elves:
                print("At least one elf died. End of game")
                return -1
            print(f'End of turn {nb_turns}')
        return nb_turns * (sum(unit.hit_points for unit in self.units['E'].values()) + sum(unit.hit_points for unit in self.units['G'].values()))

    def identify_open_squares(self, targets):
        open_squares = []
        for unit_x, unit_y in targets:
            for x, y in ((unit_x-1, unit_y), (unit_x+1, unit_y), (unit_x, unit_y-1), (unit_x, unit_y+1)):
                if 0 <= x < self.maze.shape[0] and 0 <= y < self.maze.shape[1] and self.maze[x, y] == '.':
                    open_squares.append((x, y))
        return open_squares


class Unit:
    def __init__(self, unit_type, x, y, hit_points=200, attack_power=3):
        self.type = unit_type
        self.adv_unit = 'GE'.replace(self.type, '')
        self.hit_points = hit_points
        self.x = x
        self.y = y
        self.attack_power = attack_power

    def move(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            self.x, self.y = args[0]

    def get_hit(self, power_attack):
        self.hit_points -= power_attack


class Goblin(Unit):
    def __init__(self, x, y, hit_points=200, attack_power=3):
        super().__init__('G', x, y, hit_points, attack_power)


class Elf(Unit):
    def __init__(self, x, y, hit_points=200, attack_power=3):
        super().__init__('E', x, y, hit_points, attack_power)


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        puzzle = f.read().split('\n')

    puzzle = np.array(list(map(list, puzzle)))
    print(f"The result of first star is {Grid(puzzle[:, :]).combat()}")

    elves_attack_power = 4
    while True:
        result = Grid(np.array(puzzle), elf_attack_power=elves_attack_power).combat(no_elves_loss=True)
        if result == -1:
            elves_attack_power += 1
            print(f"Elves attack power now = {elves_attack_power}")
        else:
            print(f"The result of second star is {result}")
            break
