lst = [{"a": "asdasd", "b": "asd"}, {"a": "121", "d": "123123"}]
list_symbol = [{i: len(v) for i, v in e.items()} for e in lst]

count_symbols = {}
for e in list_symbol:
    for i, v in e.items():
        if i in count_symbols:
            if v > count_symbols[i]:
                count_symbols[i] = v
        else:
            count_symbols[i] = v

for e in lst:
    f = '|'.join([
        '{' + f'{i}:{v+2}' + '}' if i in e else ' '*(v+2)
        for i, v in count_symbols.items()
    ])
    print(f'{f}'.format(**e))