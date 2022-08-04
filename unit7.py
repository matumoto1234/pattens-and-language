from typing import List
import nltk

s = "Two frogs, a father and his son, accidentally fell into a bucket of milk. They started swimming for their lives. They swam for a long time, but there seemed no hope of their getting out. The father soon gave up and drowned. The son carried on swimming. During this time, the milk had begun to form a ball of butter. Using this island of butter as a platform, he managed to hop out of the bucket."

def nouns(s) -> List[str]:
    pos_tag = nltk.pos_tag(nltk.word_tokenize(s))

    noun_list: List[str] = []

    for pos, tag in pos_tag:
        if 'NN' in tag:
            noun_list.append(pos)

    return noun_list

def plural_nouns(s) -> List[str]:
    pos_tag = nltk.pos_tag(nltk.word_tokenize(s))

    plural_noun_list: List[str] = []

    for pos, tag in pos_tag:
        if tag == 'NNS' or tag == 'NNPS':
            plural_noun_list.append(pos)

    return plural_noun_list


def singular_nouns(s) -> List[str]:
    pos_tag = nltk.pos_tag(nltk.word_tokenize(s))

    singular_noun_list: List[str] = []

    for pos, tag in pos_tag:
        if tag == 'NN' or tag == 'NNP':
            singular_noun_list.append(pos)

    return singular_noun_list


print('nouns:', *nouns(s))
print()
print('plural nouns:', *plural_nouns(s))
print()
print('singular nouns:', *singular_nouns(s))
