from unittest import TestCase

from WordSearch import WordSearch


def do_search(grid, words_to_find):
    ws = WordSearch(grid)
    output = []
    for word in words_to_find:
        if ws.is_present(word):
            output.append("found {}".format(word))
    return output


def correct_output(found_words):
    output = []
    for word in found_words:
        output.append("found {}".format(word))
    return output


class TestWordSearch(TestCase):

    def test_basic(self):
        grid = "word1gwrjk" \
               "word2sod5k" \
               "jsdkjwrrd1" \
               "jsdkjwdrd1" \
               "jsdkjw3rd1"
        words_to_find = ["word1", "word2", "word3", "thing"]
        self.assertEquals(do_search(grid, words_to_find), correct_output(["word1", "word2", "word3"]))