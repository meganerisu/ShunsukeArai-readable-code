import argparse

from dictionary_data import words


def read_word(id: int = None):
    """
    Read word from `dictionary_data.py`
    If ID is specified, return the word of ID else return whole dictionary.

    >>> read_word(0)
     上手
    """
    # word_dict = {1: something, 2: anything ...}
    word_dict = {i+1: words[i] for i in range(len(words))}

    if id is not None:
        print(f"{id}: {word_dict[id]}")
    else:
        for id, word in word_dict.items():
            print(f"{id}: {word}")


if __name__ == '__main__':
    # Argparse enable you to specify arguments from CLI like --<arg>.
    # Please refer for more details: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    # Add --id as arguments
    parser.add_argument(
        '--id', type=int, help='ID of words dictionary which store in dictionary_data.py')
    args = parser.parse_args()

    read_word(args.id)
