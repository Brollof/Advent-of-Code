from functools import reduce


with open("inp10.txt") as file:
    data = file.read()


brackets = {'{': '}', '[': ']', '(': ')', '<': '>'}
syntax_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_scores = {'(': 1, '[': 2, '{': 3, '<': 4}

syntax_error_score = 0
auto = []

for line in data.splitlines():
    stack = []
    for c in line:
        if c in '[{(<':
            stack.append(c)
        elif c != brackets[stack[-1]]:
            syntax_error_score += syntax_scores[c]
            break
        elif c == brackets[stack[-1]]:
            stack.pop()
    else:
        auto.append(reduce(lambda v, c: v * 5 + autocomplete_scores[c], reversed(stack), 0))


print(f"Part 1: {syntax_error_score}")
assert syntax_error_score == 387363

p2 = sorted(auto)[len(auto) // 2]
print(f"Part 2: {p2}")
assert p2 == 4330777059
