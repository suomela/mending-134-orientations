#!/usr/bin/env pypy3

from itertools import product

class Graph:
    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy
        self.s = [ [ 0 for x in range(self.xx) ] for y in range(self.yy) ]  # sides
        self.t = [ [ 0 for x in range(self.xx) ] for y in range(self.yy) ]  # total

    def show_sol(self, hh, vv):
        print("Given these indegrees in the boundary:")
        for y in range(self.yy):
            for x in range(self.xx):
                if y == 0 or x == 0 or y == self.yy-1 or x == self.xx-1:
                    print(self.s[y][x], end='')
                else:
                    print(' ', end='')
            print()
        print()
        print("Orient like this:")
        for y in range(self.yy):
            for x in range(self.xx):
                print(self.t[y][x], end='')
                if x != self.xx-1:
                    h = hh[y * (self.xx - 1) + x]
                    print('←→'[h], end='')
            print()
            if y != self.yy-1:
                for x in range(self.xx):
                    v = vv[y * self.xx + x]
                    print('↑↓'[v], end='')
                    if x != self.xx-1:
                        print(' ', end='')
            print()
        print()

    def solve(self):
        hh, vv = self.try_all()
        self.show_sol(hh, vv)

    def try_all(self):
        for hh in product([0,1], repeat=(self.xx-1) * self.yy):
            for vv in product([0,1], repeat=self.xx * (self.yy-1)):
                if self.check(hh, vv):
                    return (hh, vv)
        assert False

    def check(self, hh, vv):
        for y in range(self.yy):
            for x in range(self.xx):
                self.t[y][x] = self.s[y][x]
        for y in range(self.yy):
            for x in range(self.xx-1):
                h = hh[y * (self.xx - 1) + x]
                self.t[y][x + h] += 1
        for y in range(self.yy-1):
            for x in range(self.xx):
                v = vv[y * self.xx + x]
                self.t[y + v][x] += 1
        for y in range(self.yy):
            for x in range(self.xx):
                if self.t[y][x] in [0,2]:
                    return False
        return True

def main():
    g = Graph(3, 3)
    for corners in product([0,1,2], repeat=4):
        g.s[0][0] = corners[0]
        g.s[0][-1] = corners[1]
        g.s[-1][0] = corners[2]
        g.s[-1][-1] = corners[3]
        for top in product([0,1], repeat=(g.xx-2)):
            for bottom in product([0,1], repeat=(g.xx-2)):
                for x in range(g.xx-2):
                    g.s[0][x+1] = top[x]
                    g.s[-1][x+1] = bottom[x]
                for left in product([0,1], repeat=(g.yy-2)):
                    for right in product([0,1], repeat=(g.yy-2)):
                        for y in range(g.yy-2):
                            g.s[y+1][0] = left[y]
                            g.s[y+1][-1] = right[y]
                        g.solve()

main()
