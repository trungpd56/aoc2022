#!/usr/bin/env python3
import math


class Monkey:
    def __init__(self, mklines):
        lines = mklines.split("\n")
        self.items = list(map(int, lines[1].split(":")[1].split(",")))
        self.op = eval(f"lambda old: {lines[2].split('=')[-1]}")
        self.test = int(lines[3].split()[-1])
        self.true_tg = int(lines[4].split()[-1])
        self.false_tg = int(lines[5].split()[-1])
        self.cnt = 0


class MonkeyWorld:
    def __init__(self, raw, part=1):
        self.monkeys = [Monkey(mk) for mk in raw]
        self.part = part
        self.mod = math.prod([mk.test for mk in self.monkeys])

    def round(self):
        for mk in self.monkeys:
            for item in mk.items:
                val = mk.op(item)
                if self.part == 2:
                    val = val % self.mod
                else:
                    val = val // 3
                if val % mk.test == 0:
                    self.monkeys[mk.true_tg].items.append(val)
                else:
                    self.monkeys[mk.false_tg].items.append(val)
                mk.cnt += 1
            mk.items = []

    def score(self):
        sorted_monkeys = sorted(self.monkeys, key=lambda x: -x.cnt)
        return sorted_monkeys[0].cnt * sorted_monkeys[1].cnt


with open("input.txt", "r") as f:
    raw = f.read().strip().split("\n\n")

mkw = MonkeyWorld(raw)
for _ in range(20):
    mkw.round()

part1 = mkw.score()
print(f"Part1: {part1}")

mkw2 = MonkeyWorld(raw, part=2)
for _ in range(10000):
    mkw2.round()

part2 = mkw2.score()
print(f"Part1: {part2}")
