import collections
import numpy as np
import pathlib


class Grid:
    def __init__(self, maze):
        self.maze = maze
        self.units = {'G': {}, 'E': {}}
        for x, y in np.where(maze == 'G'):
            self.units['G'][(x, y)] = Goblin(self.maze, x, y)
        for x, y in np.where(maze == 'E'):
            self.units['E'][(x, y)] = Elf(self.maze, x, y)

    def shortest_path_to_ennemy(self, unit):
        """
        Return the shortest path from an unit to its closest ennemy. Tiebreaker with fewest hit points & reading order
        :param unit: an Unit (Goblin or Elf)
        :return: x, y, path
        """
        start = (unit.x, unit.y)
        queue = collections.deque([[start]])
        seen = {start}
        candidates = []
        while queue:
            path = queue.popleft()
            if len(candidates) and len(path) > len(candidates[0][2]):
                return min(candidates, key=lambda c: self.units[unit.adv_unit][c[0], c[1]].hit_points)
            x, y = path[-1]
            if self.maze[x, y] == unit.adv_unit:
                candidates.append((x, y, path))
            for x2, y2 in ((x-1, y), (x, y-1), (x, y + 1), (x+1, y)):
                if 0 <= x2 < self.maze.shape[0] and 0 <= y2 < self.maze.shape[1] and self.maze[x2, y2] != '#' and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))


class Combat:
    def __init__(self, grid):
        self.grid = grid


class Unit:
    def __init__(self, unit_type, x, y, hit_points=3, attack_power=200):
        self.type = unit_type
        self.adv_unit = 'GE'.replace(self.type, '')
        self.hit_points = hit_points
        self.x = x
        self.y = y
        self.attack_power = attack_power

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_hit(self, power_attack):
        self.hit_points -= power_attack


class Goblin(Unit):
    def __init__(self, x, y, hit_points=3, attack_power=200):
        super().__init__('G', x, y, hit_points, attack_power)


class Elf(Unit):
    def __init__(self, x, y, hit_points=3, attack_power=200):
        super().__init__('E', x, y, hit_points, attack_power)


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        puzzle = f.read().split('\n')

    puzzle = np.array(list(map(list, puzzle)))
