#!/usr/bin/python3

if __name__ == "__main__":

    import importlib
    _import = importlib.import_module('hidden_4')

    byte = dir(_import)

    for count in enumerate(byte):
        if count[0] == '_':
            continue

        print(f"{count}")
