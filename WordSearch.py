class WordSearch(object):
    def __init__(self, grid):
        # String containing the entire grid, row concatinated with no delimeter
        # Fixed ROW LENGTH,
        # Random chars up to 24, avg 9, nothing special
        self.__ROW_LENGTH = 10  # 10000 chars
        self.__horizontals = grid
        self.__verticals = grid  # char 0,ROW_LENGTH,2*ROW_LENGTH...
        self.__grid = []
        sub_arr = []
        for i, char in enumerate(grid):
            if i % self.__ROW_LENGTH == 0 and i != 0:
                self.__grid.append(sub_arr)
                sub_arr = []
            sub_arr.append(char)
        self.__grid.append(sub_arr)
        print(self.__grid)

    def is_present(self, word):
        # Try word from within the grid to see what works?
        # Horizontal is simply is word in string
        return word in self.__horizontals
        # return True


if __name__ == "__main__":

    grid = "word1gerjkword2sad5kjsdkjword1"  # 10^4 letters in each direction
    words_to_find = ["word1", "word2", "word3"]  # 10^6 words
    ws = WordSearch(grid)

    for word in words_to_find:
        if ws.is_present(word):
            print("found {}".format(word))
