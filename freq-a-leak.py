def histoblamo(text):
    word_count = {}

    for word in text:
        try:
            word_count[word] += 1
        except KeyError:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    sample_text = ["hi", "doge", "i", "see", "doge", "hi"]
    print(histoblamo(sample_text))
