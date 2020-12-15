class WordSearch(object):
    def __init__(self, grid):
        self.__ROW_LENGTH = 10
        self.__horizontals = grid
        self.__verticals = ""
        self.__row_width = int(len(grid) / self.__ROW_LENGTH)
        for i in range(self.__ROW_LENGTH):
            for j in range(0, len(grid), self.__ROW_LENGTH):
                self.__verticals += grid[j + i]

    def is_present(self, word):
        return word in self.__horizontals or word in self.__verticals