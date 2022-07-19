from sys import stdin
from typing import List


def is_inverted_negative_sentence(words: List[str]):
    if 'not' in words:
        return False

    do_list = ['do', 'did', 'does']

    assert 'XXX' in words, 'please includes "XXX" in the input sentence.'

    idx = words.index('XXX')
    is_XXX_after_do_found = idx+1 < len(words) and words[idx+1] in do_list

    if is_XXX_after_do_found:
        return True

    return False


def is_affirmative_sentence(words: List[str]):
    return not 'not' in words


def is_negative_or_questionable_sentence(words: List[str]):
    return 'not' in words or words[-1][-1] == '?'


def replace_list_str(words: List[str], target: str, replacement: str) -> List[str]:
    new_words: List[str] = []

    for word in words:
        if word == target:
            new_words.append(replacement)
        else:
            new_words.append(word)

    return new_words



def main():
    print('please input!')
    print('input ends Ctrl-D or EOF.')

    words: List[str] = []

    for line in stdin:
        one_line_words = line.split(' ')

        for word in one_line_words:
            words.append(word)


    if is_inverted_negative_sentence(words):

        joined_str = ' '.join(replace_list_str(words, 'XXX', 'nobody'))
        print(joined_str.capitalize(), end='')

    else:
        joined_str = ' '.join(replace_list_str(words, 'XXX', 'everybody'))
        print(joined_str.capitalize(), end='')

        if is_affirmative_sentence(words):
            joined_str = ' '.join(replace_list_str(words, 'XXX', 'somebody'))
            print(joined_str.capitalize(), end='')

        if is_negative_or_questionable_sentence(words):
            joined_str = ' '.join(replace_list_str(words, 'XXX', 'anybody'))
            print(joined_str.capitalize(), end='')

main()
