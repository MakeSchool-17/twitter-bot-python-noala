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
    distribution_list = []
    distribution_range = 0

    for word, freq in histogram_creator_return.items():
        if word not in distribution_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            distribution_list.append((word, upper_limit))
    return distribution_list


def sample_from_distribution(cumulative_distribution_return):
    token_tuple = cumulative_distribution_return[-1]
    tokens = token_tuple[-1]

    for word, limit in cumulative_distribution_return:
        rand_index = random.randint(0, tokens - 1)
        if rand_index < limit:
            return word


def main():
    histogram_creator_returns = histogram_creator(sys.argv[1:])
    cum_distribution_returns = cumulative_distribution(histogram_creator_returns)
    return sample_from_distribution(cum_distribution_returns)


def relative_probability():
    check_list = []
    for result in range(10000):
        sample_from_distribution = main()
        check_list.append(sample_from_distribution)
    print(histogram_creator(check_list))
    return histogram_creator(check_list)


if __name__ == '__main__':
    relative_probability()
