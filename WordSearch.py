class WordSearch(object):
    def __init__(self, grid):
        # String containing the entire grid, row concatenated with no delimiter
        # Fixed ROW LENGTH,
        # Random chars up to 24, avg 9, nothing special
        self.__ROW_LENGTH = 10  # 10000 chars
        self.__horizontals = grid
        self.__verticals = ""  # char 0,ROW_LENGTH,2*ROW_LENGTH...
        self.__row_width = int(len(grid) / self.__ROW_LENGTH)
        for i in range(self.__ROW_LENGTH):  # As many down as there are across
            for j in range(0, len(grid), self.__ROW_LENGTH): # 0,10... 1,11... 2,12...
                self.__verticals += grid[j + i]

    def is_present(self, word):
        # Try word from within the grid to see what works?
        # Horizontal is simply is word in string
        return word in self.__horizontals or word in self.__verticals
        # return True


if __name__ == "__main__":
    # 10^4 letters in each direction
    grid = "word1gwrjk" \
           "word2sod5k" \
           "jsdkjwrrd1" \
           "jsdkjwdrd1" \
           "jsdkjw3rd1"
    words_to_find = ["word1", "word2", "word3", "thing"]  # 10^6 words
    ws = WordSearch(grid)

    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))