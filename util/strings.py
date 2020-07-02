def get_line(line, symbol):
    return line[line.count(symbol) + 1:len(line) - 1].strip()

def edit_line(line):
    return line.lower().replace(' ', '-').replace('/', '')