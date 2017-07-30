class OurWord():
    def __init__(self):
        self.word = input('Type a word: ')
        self.actual_word = len(self.word) * '*'
        print(10 * "\n")
        print(self.actual_word)
        self.wrong_guesses = 0
        self.left = len(self.word)
        self.list_of_occurrences = []

    def __del__(self):
        print('Gameover')

    def create_list(self):
        for i in range(27):
            self.list_of_occurrences.append(False)

    def end_game(self, win):
        if win:
            print('Word guessed correctly!')
        else:
            print('You died trying!')

    def check_one_letter(self, letter):
        hit = False
        if self.list_of_occurrences[ord(letter) - ord("a")]:
            print('You picked that one before!')
            return 0
        else:
            self.list_of_occurrences[ord(letter) - ord("a")] = True
        for i, c in enumerate(self.word):
            if c == letter:
                temp = list(self.actual_word)
                temp[i] = letter
                self.actual_word = ''.join(temp)
                self.left -= 1
                hit = True
        if self.left == 0:
            return 1
        if not hit:
            print('Wrong one')
            self.wrong_guesses += 1
            if self.wrong_guesses == 9:
                return 2
        return 0

    def show_actual_word(self):
        print(self.actual_word)

newGame = OurWord()
newGame.create_list()
check = 0
while check == 0:
    letter = input('Guess a letter: ')
    check = newGame.check_one_letter(letter)
    newGame.show_actual_word()
    if(check == 1):
        newGame.end_game(True)
    if(check == 2):
        newGame.end_game(False)