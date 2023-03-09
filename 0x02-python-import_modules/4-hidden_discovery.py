#!/usr/bin/python3

if __name__ == "__main__":

    import marshal

    with open('hidden_4.pyc', 'rb') as f:
        code = marshal.load(f)

    names = code.co_names

    filt_names = [name for name in names if not name.startswith('_')]

    for name in filt_names:
        print(name)
