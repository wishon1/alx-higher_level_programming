#!/usr/bin/python3

if __name__ == "__main__":

    import importlib
    _import = importlib.import_module('hidden_4')

    byte = dir(_import)

    for count, name in enumerate(byte):
        if name[0] == '_':
            continue

        print(f"{name}")
