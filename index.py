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
                        'str': strings.get_line(line, symbol),
                    }
                )
    else:
        raise Exception('This is not a Markdown file')
    return data


# for el in data:
#     print('#' * el['count'] + strings.edit_line(el['str']))
