import random
import sys


def randy_dict():
    dictionary = open('/usr/share/dict/words').read().split('\n')
    rand_index = random.randint(0, len(dictionary) - 1)

    return dictionary[rand_index]

if __name__ == '__main__':
    print(' '.join([randy_dict() for i in range(int(sys.argv[1]))]))
