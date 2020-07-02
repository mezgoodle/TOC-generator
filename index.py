import pathlib
from util import consts

def read_f(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


symbol = '#'
data = []
path = 'README.md'

if pathlib.Path(path).suffix.lower() == consts.extension:
    for line in read_f('README.md'):
        if line.startswith(symbol):
            data.append(
                {
                    'count': line.count(symbol),
                    'str': line[line.count(symbol) + 1:len(line) - 1],
                }
            )
    print(data)
else:
    raise Exception('This is not a Markdown file')
