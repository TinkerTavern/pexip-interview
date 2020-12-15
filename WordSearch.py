class WordSearch(object):
    def __init__(self, grid):
        self.__ROW_LENGTH = int(len(grid) ** 0.5)  # Intended to be fixed, but dynamically determined for testing
        self.__horizontals = [grid[i:i + self.__ROW_LENGTH] for i in range(0, len(grid), self.__ROW_LENGTH)]
        self.__verticals = [''.join([grid[j + i] for j in range(0, len(grid), self.__ROW_LENGTH)]) for i in range(self.__ROW_LENGTH)]

    def is_present(self, word):
        return any(word in line for line in self.__horizontals) or any(word in line for line in self.__verticals)


"""
Bonus Question:
The primary place where parallelisation could be used to speed up execution with a multi core system is with the class usage code:

for word in words_to_find:
    if ws.is_present(word):
        print "found {}".format(word)

Provided there wasn't a requirement to loop through the words in a specific order, then you could simply break the list into n sub-lists, 
where n is the number of threads capable of being used in your system. This has been demonstrated and tested in the test_WordSearch.py file

There are two other potential places for multithreading/multiprocessing could be beneficial from within the code:
1) Determination of horizontals/verticals (~4/5) (see testing/multi-processed-init branch)
2) Checking each any() from is_present (see testing/multi-processed-is-present branch)

However, given these operations individually take a very small amount of time, there's a high probability that it would in fact slow the processing down

Note: It's important to consider data access when using threading, however in the above example, data is only ever being read
"""