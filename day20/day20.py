#!/usr/bin/env python3
from collections import deque


def mix(nums):
    for i in range(len(nums)):
        while True:
            if nums[0][0] == i:
                break
            nums.append(nums.popleft())
        num = nums.popleft()
        n = num[1] % len(nums)
        for i in range(n):
            nums.append(nums.popleft())
        nums.append(num)
    return nums


def score(nums):
    while True:
        if nums[0][1] == 0:
            break
        nums.append(nums.popleft())

    return sum(nums[i][1] for i in (1000, 2000, 3000))


with open('input.txt', 'r') as f:
    numbers = [int(line) for line in f.readlines()]

nums = deque(enumerate(numbers))
part1 = score(mix(nums))
print(f'Part1: {part1}')

nums2 = deque((i, n*811589153) for i, n in enumerate(numbers))
for _ in range(10):
    nums2 = mix(nums2)

part2 = score(nums2)
print(f'Part2: {part2}')
