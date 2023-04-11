#!/usr/bin/env python3

score = {"Win": 6, "Lose": 0, "Draw": 3, "Rock": 1, "Paper": 2, "Scissors": 3}

enemy = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

you = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

rules = {
    "Rock Rock": "Draw",
    "Rock Paper": "Win",
    "Rock Scissors": "Lose",
    "Paper Rock": "Lose",
    "Paper Paper": "Draw",
    "Paper Scissors": "Win",
    "Scissors Rock": "Win",
    "Scissors Paper": "Lose",
    "Scissors Scissors": "Draw",
}

rules2 = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}

with open("input.txt", "r") as f:
    lines = f.readlines()

total_score = 0
total_score2 = 0
for line in lines:
    toks = line.split()
    key = f"{enemy[toks[0]]} {you[toks[1]]}"
    total_score += score[you[toks[1]]] + score[rules[key]]
    for k, v in rules.items():
        if v == rules2[toks[1]] and k.startswith(enemy[toks[0]]):
            total_score2 += score[k.split()[1]] + score[rules2[toks[1]]]


part1 = total_score
print(f"Part1: {part1}")

part2 = total_score2
print(f"Part2: {part2}")
