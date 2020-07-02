import pathlib
from util import consts, strings


def read_f(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


def create_data(path):
    data = []
    symbol = consts.SYMBOL
    if pathlib.Path(path).suffix.lower() == consts.EXTENSION:
        for line in read_f(path):
            if line.startswith(symbol):
                data.append(
                    {
                        'count': line.count(symbol),
                        'str': strings.edit_line(strings.get_line(line, symbol)),
                    }
                )
    else:
        raise Exception('This is not a Markdown file')
    return data

data = create_data('readme.md')
for el in data:
    print('#' * el['count'] + el['str'])
