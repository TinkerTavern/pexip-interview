import random
import string
import threading
from datetime import datetime
from unittest import TestCase

from WordSearch import WordSearch


def do_search(grid, words_to_find):
    ws = WordSearch(grid)
    output = []
    start_present = datetime.now()
    for word in words_to_find:
        if ws.is_present(word):
            output.append("found {}".format(word))
    print("Standard = ", datetime.now() - start_present)
    return output


def do_search_multi(grid, words_to_find):
    n = 16  # no of threads
    size = int(len(words_to_find) / n)
    ws = WordSearch(grid)

    threads = []
    start = datetime.now()
    for i in range(n):
        arr = words_to_find[i * size:(i + 1) * size]

    thr = threading.Thread(target=find_words, args=(ws, arr,))
    thr.start()
    threads.append(thr)

    for thread in threads:
        thread.join()
    print("Threaded = ", datetime.now() - start)


def find_words(ws, list):
    output = []
    for word in list:
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

    def test_small(self):
        letters = string.ascii_lowercase
        grid = ''.join(random.choice(letters) for _ in range(10000))
        words_to_find = [(''.join(random.choice(letters) for _ in range(random.randint(1, 12)))) for _ in
                         range(10000)]
        start = datetime.now()
        self.assertEquals(do_search(grid, words_to_find), correct_output([""]))
        print(datetime.now() - start)

    def test_med(self):
        letters = string.ascii_lowercase
        grid = ''.join(random.choice(letters) for _ in range(1000000))
        words_to_find = [(''.join(random.choice(letters) for _ in range(random.randint(1, 15)))) for _ in
                         range(100000)]
        start = datetime.now()
        do_search_multi(grid, words_to_find), correct_output([""])
        self.assertEquals(do_search(grid, words_to_find), correct_output([""]))
        print(datetime.now() - start)

    def test_full(self):
        letters = string.ascii_lowercase
        grid = ''.join(random.choice(letters) for _ in range(100000000))  # 10^4 in each direction
        words_to_find = [(''.join(random.choice(letters) for _ in range(random.randint(1, 24)))) for _ in
                         range(1000000)]
        print("Start testing")
        start = datetime.now()
        self.assertEquals(do_search(grid, words_to_find), correct_output([""]))
        print(datetime.now() - start)
