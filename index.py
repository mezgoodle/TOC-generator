def read_f(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data


print(read_f('LICENSE'))