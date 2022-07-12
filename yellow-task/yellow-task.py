from sys import stdin
from typing import List


def is_affirmative(words: List[str]):
    # TODO: if words are affirmative, return True.
    return True


def is_specific(target: List[str]):
    # TODO: if target is specific, return True.
    #       else, return False.
    return True


def is_all_people(number_of_person_in_a_group: int):
    # TODO: if number of person in a group is all people, return True.
    #       else, return False.
    return True


def extract_target(words: List[str]) -> List[str]:
    # TODO: extract target of sentences.
    return words


def analyze_number_of_person(target: List[str]) -> int:
    # TODO: analyze number of person in target.
    return 1


def main():
    words: List[str] = []

    for line in stdin:
        one_line_words = line.split(' ')

        for word in one_line_words:
            words.append(word)


    if is_affirmative(words):
        target: List[str] = extract_target(words)

        if is_specific(target):
            number_of_person: int = analyze_number_of_person(target)

            if is_all_people(number_of_person):
                print('everybody')
            else:
                print('somebody')

        else:
            print('anybody')

    else:
        print('nobody')


main()
