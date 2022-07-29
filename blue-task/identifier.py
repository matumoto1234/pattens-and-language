from sys import stdin
from typing import List

class Identifier:
    def __is_inverted_negative_sentence(self, words: List[str]):
        if 'not' in words:
            return False

        do_list = ['do', 'did', 'does']

        assert 'XXX' in words, 'please includes "XXX" in the input sentence.'

        idx = words.index('XXX')
        is_XXX_after_do_found = idx+1 < len(words) and words[idx+1] in do_list

        if is_XXX_after_do_found:
            return True

        return False


    def __is_affirmative_sentence(self, words: List[str]):
        return not 'not' in words


    def __is_negative_or_questionable_sentence(self, words: List[str]):
        return 'not' in words or words[-1][-1] == '?'


    def __replace_list_str(self, words: List[str], target: str, replacement: str) -> List[str]:
        new_words: List[str] = []

        for word in words:
            if word == target:
                new_words.append(replacement)
            else:
                new_words.append(word)

        return new_words


    # str.capitalize()を使うと'Does I?'->'Does i?'みたいに途中の大文字が変更されるので自作
    # 最初の文字を大文字にするだけ
    def __capitalize(self, s: str) -> str:
        if not s:
            return s

        return s[0].upper() + s[1:len(s)]


    def analyze(self, words: List[str]) -> List[List[str]]:
        if self.__is_inverted_negative_sentence(words):
            joined_str = ' '.join(self.__replace_list_str(words, 'XXX', 'nobody'))
            return [self.__capitalize(joined_str)]

        # 最初の行に出力すると左側にずれるので最初に改行
        result = ['\n']

        joined_str = ' '.join(self.__replace_list_str(words, 'XXX', 'everybody'))
        result.append(self.__capitalize(joined_str) + '\n')

        if self.__is_affirmative_sentence(words):
            joined_str = ' '.join(self.__replace_list_str(words, 'XXX', 'somebody'))
            result.append(self.__capitalize(joined_str) + '\n')

        if self.__is_negative_or_questionable_sentence(words):
            joined_str = ' '.join(self.__replace_list_str(words, 'XXX', 'anybody'))
            result.append(self.__capitalize(joined_str) + '\n')

        return result
