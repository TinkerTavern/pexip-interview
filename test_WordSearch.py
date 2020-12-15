import multiprocessing
import random
import string
from datetime import datetime
from unittest import TestCase

from WordSearch import WordSearch


def standard_search(ws, words_to_find):
    output = []
    for word in words_to_find:
        if ws.is_present(word):
            output.append("found {}".format(word))
    return output


def multi_processing_search(ws, words_to_find):
    processors = 32
    subsection_size = int(len(words_to_find) / processors)
    processes = []
    for i in range(processors):
        arr = words_to_find[i * subsection_size:(i + 1) * subsection_size]

        process = multiprocessing.Process(target=find_words, args=(ws, arr,))
        process.start()
        processes.append(process)

    for thread in processes:
        thread.join()


def find_words(ws, list):
    output = []  # Using array here simply for simplicity in testing
    for word in list:
        if ws.is_present(word):
            output.append("found {}".format(word))
    return output


def correct_output(found_words):
    output = []
    for word in found_words:
        output.append("found {}".format(word))
    return output


def speed_test_sample(grid_size, max_word_length, no_of_words):
    letters = string.ascii_lowercase
    grid = ''.join(random.choice(letters) for _ in range(grid_size))
    words_to_find = [(''.join(random.choice(letters) for _ in range(random.randint(1, max_word_length)))) for _ in range(no_of_words)]
    ws = WordSearch(grid)

    start = datetime.now()
    standard_search(ws, words_to_find)
    single_time = datetime.now() - start

    start = datetime.now()
    multi_processing_search(ws, words_to_find)
    multi_time = datetime.now() - start

    return multi_time, single_time


class TestWordSearch(TestCase):

    def test_basic_functionality(self):
        grid = "catsdgdrjk" \
               "wordtsodtk" \
               "jsdkjwgrdt" \
               "jsdkjwdrdt" \
               "jsdkjwtrdt" \
               "aajgyhksdg" \
               "jsdhellodt" \
               "jsdkjwtthi" \
               "ngdkjwtrdt" \
               "jsstuffrdt"
        words_to_find = ["cats", "dog", "hello", "thing", "dynamic"]  # 'thing' is there, but looped over 2 lines
        ws = WordSearch(grid)
        self.assertEquals(standard_search(ws, words_to_find), correct_output(["cats", "dog", "hello"]))

    def test_speed_small_sample(self):
        multi_time, single_time = speed_test_sample(10000, 12, 10000)
        self.assertLess(single_time, multi_time, "Single processing method should be faster for a small dataset")

    def test_speed_med_sample(self):
        multi_time, single_time = speed_test_sample(1000000, 15, 100000)
        self.assertLess(multi_time, single_time, "Multi processing method should be faster for a medium dataset")

    # Note: This test can take quite a while, particularly for the non multi threaded approach
    def test_speed_full_sample(self):
        multi_time, single_time = speed_test_sample(100000000, 24, 1000000)
        self.assertLess(multi_time, single_time, "Multi processing method should be faster for the largest dataset")
