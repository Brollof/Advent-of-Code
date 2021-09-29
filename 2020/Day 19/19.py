import re


with open('input.txt') as file:
    data = file.read()


def parse():
    global data
    rules = {}
    rules_str, msgs = data.split('\n\n')

    for rule in rules_str.splitlines():
        n, matches = rule.split(':')
        rules[int(n)] = matches.replace('"', '') + ' '

    return rules, msgs.splitlines()


rules, msgs = parse()

# part 2, comment this to get part 1
rules[8] = ' 42 | 42 8 '
rules[11] = ' 42 31 | 42 11 31 '


def replace(key, rep_key):
    repl = f" ( {rules[rep_key]} ) " if "|" in rules[rep_key] else f" {rules[rep_key]} "
    rules[key] = rules[key].replace(f" {rep_key} ", repl)


def gen_rule0():
    safe_break = 15
    while any(c.isdigit() for c in rules[0]):
        safe_break -= 1
        if not safe_break:
            print("safe break")
            break

        for key in rules:
            replace(0, key)

    return rules[0].replace(' ', '')


rule0 = gen_rule0()
cnt = 0

for line in msgs:
    if m := re.match(rf'^{rule0}$', line):
        cnt += 1

print(cnt)

