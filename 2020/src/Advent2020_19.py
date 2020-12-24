# Advent of Code 2020
#
# From https://adventofcode.com/2020/day/19
#
import re

# Extract inputs
filename = ''
data = [x.split('\n') for x in open(f'../inputs/Advent2020_19{filename}.txt', 'r').read().split('\n\n')]
msg = data[1]

rules = {part[0]: part[1].replace('\"', '') for part in (rule.split(': ') for rule in data[0])}
for rule in rules.keys():
    val = rules[rule].split()
    for ix, v in enumerate(val):
        if v.isdigit():
            val[ix] = f"({v})"
    if len(val) == 1 and v.isalpha():
        rules[rule] = v
    else:
        rules[rule] = f"({')|('.join(''.join(val).split('|'))})"

knowns = {k: v for k, v in rules.items() if not bool(re.search(r'\d', v))}
unknowns = {k: v for k, v in rules.items() if bool(re.search(r'\d', v))}
prev = 0
while unknowns:
    # if len(unknowns) == prev:
    #     break
    prev = len(unknowns)
    to_delete = []
    for k, v in unknowns.items():
        numbers = re.findall(r'\d+', v)
        for number in sorted(numbers, reverse=True):
            if number in knowns:
                if ' ' in knowns[number] and v[0] != '(' and v[-1] != ')':
                    v = re.sub(f"\\b{number}\\b", knowns[number], v)
                else:
                    v = re.sub(f"\\b{number}\\b", knowns[number], v)
        if bool(re.search(r'\d', v)):
            unknowns[k] = v
        else:
            knowns[k] = v
            to_delete.append(k)
            break
    # print("\n\nKnowns\n", knowns, "\n\nUnknowns\n", unknowns)

    for to_del in to_delete:
        del unknowns[to_del]

reg = f"^{knowns['0'].replace(' ', '')}$"

print(sum(bool(re.match(reg, message)) for message in msg))

knowns = {k: v for k, v in rules.items() if not bool(re.search(r'\d', v))}
unknowns = {k: v for k, v in rules.items() if bool(re.search(r'\d', v))}

unknowns["8"] = "42 | 42 42 | 42 42 42 | 42 42 42 | 42 42 42 42 42"
unknowns["11"] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31"
prev = 0
while unknowns:
    if len(unknowns) == prev:
        break
    prev = len(unknowns)
    to_delete = []
    for k, v in unknowns.items():
        numbers = re.findall(r'\d+', v)
        for number in sorted(numbers, reverse=True):
            if number in knowns:
                if ' ' in knowns[number] and v[0] != '(' and v[-1] != ')':
                    v = re.sub(f"\\b{number}\\b", knowns[number], v)
                else:
                    v = re.sub(f"\\b{number}\\b", knowns[number], v)
        if bool(re.search(r'\d', v)):
            unknowns[k] = v
        else:
            knowns[k] = v
            to_delete.append(k)
            break
    # print("\n\nKnowns\n", knowns, "\n\nUnknowns\n", unknowns)

    for to_del in to_delete:
        del unknowns[to_del]

reg = f"^{knowns['0'].replace(' ', '')}$"

print(sum(bool(re.match(reg, message)) for message in msg))