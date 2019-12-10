from src.word_frequency.input import Input


def count_word_frequency(paragraph: str) -> str:
    words = paragraph.split()

    sorted_inputs = count_words(words)

    return render_word_frequency(sorted_inputs)


def count_words(words):
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_inputs = []
    for word, count in word_dict.items():
        sorted_inputs.append(Input(word, count))
    return sorted(sorted_inputs, key=lambda w: w.count, reverse=True)


def render_word_frequency(sorted_inputs):
    return '\n'.join(map(lambda s: f'{s.word} {s.count} ', sorted_inputs)).strip()


if __name__ == '__main__':
    print(count_word_frequency("the the is"))
