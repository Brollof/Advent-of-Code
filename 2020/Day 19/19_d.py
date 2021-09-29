import re

tests = [
    ('89 12', True),
    ('189 12', False),
    ('90 89', True),
    ('90 189', False),
    ('12 89)', True),
    ('12 189)', False),
    ('(89 12', True),
    ('(189 12', False),
    ('890 12', False)
]

regex = re.compile(r'\b89\b')

for s, expected in tests:
    if m := regex.search(s):
        print(f'match on "{s}", should be {expected}')

