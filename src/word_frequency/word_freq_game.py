from src.word_frequency.input import Input


def count_word_frequency(paragraph: str) -> str:
    words = paragraph.split()
    sorted_inputs = count_words(words)
    return render_word_frequency(sorted_inputs)


def count_words(words):
    inputs = map(lambda w: Input(w, words.count(w)), set(words))
    return sorted(inputs, key=lambda w: w.count, reverse=True)


def render_word_frequency(sorted_inputs):
    return '\n'.join(map(lambda s: f'{s.word} {s.count} ', sorted_inputs)).strip()


if __name__ == '__main__':
    print(count_word_frequency("the the is"))
