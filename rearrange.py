import random
import sys


def random_all_the_things(string):
    new_list = []

    for i in range(0, len(string)):
        rand_index = random.randint(0, len(string) - 1)

        new_list.append(string[rand_index])
        string.remove(string[rand_index])

    return new_list

if __name__ == '__main__':
    print(' '.join(random_all_the_things(sys.argv[1:])))
