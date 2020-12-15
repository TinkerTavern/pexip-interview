class WordSearch(object):
    def __init__(self, grid):
        self.__ROW_LENGTH = int(len(grid) ** 0.5)  # Intended to be fixed, but dynamically determined for testing
        self.__horizontals = [grid[i:i + self.__ROW_LENGTH] for i in range(0, len(grid), self.__ROW_LENGTH)]
        self.__verticals = [''.join([grid[j + i] for j in range(0, len(grid), self.__ROW_LENGTH)]) for i in range(self.__ROW_LENGTH)]

    def is_present(self, word):
        return any(word in line for line in self.__horizontals) or any(word in line for line in self.__verticals)
