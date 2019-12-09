from src.word_frequency.input import Input


def count_word_frequency(paragraph: str) -> str:
    words = paragraph.split()

    input_list = []
    for word in words:
        input_list.append(Input(word, 1))

    word_dict = {}
    for input_item in input_list:
        if input_item.value in word_dict:
            word_dict[input_item.value].append(input)
        else:
            word_dict[input_item.value] = [input]

    new_list = []
    for word, value in word_dict.items():
        count = len(word_dict[word])
        new_list.append(Input(word, count))

    sorted_list = sorted(new_list, key=lambda x: x.count, reverse=True)

    return render_word_frequency(sorted_list)


def render_word_frequency(sorted_list):
    result = ''
    for item in sorted_list:
        result += f'{item.value} {item.count} \n'
    return result.strip()


if __name__ == '__main__':
    print(count_word_frequency("the the is"))
