#!/usr/bin/env python
import sys
import os
import pandas as pd

def main():
    """

    :returns: TODO

    """
    #  if len(sys.argv) not in [2, 3]:
        #  print('usage: mark symbol [path]')
        #  return 1

    path = '.'
    #  if len(sys.argv) == 3:
        #  path = sys.argv[2]

    #  abspath = os.path.abspath(path)

    file_to_use = ''
    if os.path.isfile(abspath):
        file_to_use = FILESPATH
    elif os.path.isdir(abspath):
        file_to_use = DIRPATH
    else:
        return 1


    sym = sys.argv[1]
    data = pd.read_csv(file_to_use, sep='\t', index_col=0)

    if sym in data.index:
        print("{} exists in {} as: {}".format(sym, file_to_use, data.loc[sym]))
        var = ''
        while var not in ['y', 'n']:
            var = input('Would you replace it? [y/n]')

        if var == 'n':
            return 0

    data.loc[sym] = abspath
    data.to_csv(file_to_use, sep='\t')
    print('Done. Run shortcuts; source ~/.zshrc to activate')
    return 0


if __name__ == "__main__":
    main()




