#!/usr/bin/env python3


class Console:
    def __init__(self, lines):
        self.lines = lines
        self.x = 1
        self.cycle = 0
        self.signal = 0
        self.pixels = {}

    def step(self):
        r = self.cycle // 40
        c = self.cycle % 40
        self.cycle += 1
        if self.x - 1 <= c <= self.x + 1:
            self.pixels[(r, c)] = "#"
        else:
            self.pixels[(r, c)] = " "
        if (self.cycle - 20) % 40 == 0:
            self.signal += self.x * self.cycle

    def addx(self, v):
        self.step()
        self.step()
        self.x += v

    def noop(self):
        self.step()

    def run(self):
        for line in self.lines:
            toks = line.strip().split()
            if toks[0] == "noop":
                self.noop()
            elif toks[0] == "addx":
                self.addx(int(toks[1]))

    def display(self):
        for r in range(6):
            for c in range(40):
                print(self.pixels[(r, c)], end="")
            print()


with open("input.txt", "r") as f:
    lines = f.readlines()

console = Console(lines)
console.run()

part1 = console.signal
print(f"Part1: {part1}")

console.display()
