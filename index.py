import pathlib
from util import consts, strings


def read_f(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


symbol = consts.symbol
data = []
path = input()


if pathlib.Path(path).suffix.lower() == consts.extension:
    for line in read_f(path):
        if line.startswith(symbol):
            data.append(
                {
                    'count': line.count(symbol),
                    'str': strings.get_line(line, symbol),
                }
            )
else:
    raise Exception('This is not a Markdown file')

for el in data:
    print('#' * el['count'] + strings.edit_line(el['str']))