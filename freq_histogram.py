import random
import sys


def histogram_creator(words_from_user_input):
    word_counts = {}

    for word in words_from_user_input:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1
    return word_counts


def cumulative_distribution(histogram_creator_return):
    cum_list = []
    distribution_range = 0

    for word, freq in histogram_creator_return.items():
        if word not in cum_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            cum_list.append((word, upper_limit))
    return cum_list


def sample_from_distribution(cumulative_distribution_return):
    tokens = cumulative_distribution_return[-1][-1]

    for word, limit in cumulative_distribution_return:
        rand_index = random.randint(0, tokens - 1)
        if rand_index < limit:
            return word


def main():
    histogram_creator_returns = histogram_creator(sys.argv[1:])
    cum_distribution_returns = cumulative_distribution(histogram_creator_returns)
    return sample_from_distribution(cum_distribution_returns)


if __name__ == '__main__':
    print(main())
