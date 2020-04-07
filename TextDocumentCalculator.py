""" Implementation of a calculator which takes a file as input and writes

- amount of words
- amount of characters including spaces
- amount of keyboard strokes
- distribution of words (top 10)
- distribution of characters (top 10)
- average word length

into a pickle file.
"""

#:#:#:# - - - - - - - - - CLASS / METHODS

class Calculator:

    def __init__(self):
        """Open file and save it in variable"""
        
        with open('Morgen_Kinder.txt', 'r', encoding="utf-8-sig") as f:
            # readlines() is faster but readline() is more memory efficient
            self.content = f.readlines()

        self.split_content = self.splitter()
        """print(self.content)
        print(type(self.content))
        print(self.split_content)
        print(type(self.split_content))"""
        
        self.amount_lines = len(self.content)

    def splitter(self):
        """Splits whole content into seperate words and deletes anything that
        doesnt belong to the actual word"""
        delimiters = ['\n', ' ', ',', '.', '?', '!', ':', "'", '´', '`', ';',
                      '(', ')', '[', ']', '{', '}', '#', '@', '%', '&', '-',
                      '’', '–', 'insert_anything_else']
        words = self.content
        for delimiter in delimiters:
            new_words = []
            for word in words:
                new_words += word.split(delimiter)
                words = new_words
        # Filters empty strings
        words = list(filter(None, words))
        counter = -1
        # Filters words have a length smaller than 2
        for word in words:
            counter += 1
            if len(word) <= 1:
                del words[counter]
        #print(words)
        return words

    def words(self):
        amount_words = len(self.split_content)
        #print(amount_words)
            
    def characters_spaces(self):
        """Counts amount of characters including spaces"""
        characters_spaces = 0
        for x in range(0, self.amount_lines):
            characters_spaces_line = self.content[x].rstrip()
            characters_spaces += len(characters_spaces_line)
        print(characters_spaces)

    def characters_no_spaces(self):
        """Counts amount of characters excluding spaces"""
        line_counter = 0
        counter = []
        for x in range(0, self.amount_lines):
            # Grab xth line
            line = self.content[x]
            # Separate each line into a list of separated words
            separated_words = line.split()
            amount_seperated_words = len(separated_words)
            for y in range(0, amount_seperated_words):
                # iterate through every word. Splitting will delete spaces
                characters = len(separated_words[y])
                counter.append(characters)
        character_no_spaces = sum(counter)
        #print(character_no_spaces)

    def character_counter(self):
        """Counts how often each character is used in the text file"""
        # convert list into string to be able to use the lower()-method
        self.content = ''.join(self.content)
        lowercase_content = self.content.lower()
        character_counter = {}
        # fill the dictionary
        for char in lowercase_content:
            if char in character_counter:
                character_counter[char] += 1
            else:
                character_counter[char] = 1
        self.distribution(character_counter)

    def word_counter(self):
        """Counts how often each character is used in the text file"""
        separated_words = [x.lower() for x in self.split_content]
        word_counter = {}
        # fill the dictionary
        for word in separated_words:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        self.distribution(word_counter)

    def distribution(self, passed_dictionary):
        dictionary = passed_dictionary
        distribution = []
        # print(dictionary)
        for x in range(0, 10):
            max_key = max(dictionary, key=dictionary.get)
            #print(max_key)
            max_key_value = dictionary.get(max_key)
            #print(max_key_value)
            del dictionary[max_key]

    def average_word_length(self):
        """Shows average word length"""
        amount_characters = 0
        amount_words = len(self.split_content)
        for x in range(0, amount_words):
            amount_characters += len(self.split_content[x])
        average = amount_characters / amount_words
        #print(average)
        
    def writer(self):
        """Writes calculated data into structured data file (JSON or pickle)"""
        pass

#:#:#:# - - - - - - - - - MAIN FUNCTIONS
    
def main():
    calculator = Calculator()

    calculator.words()
    calculator.characters_spaces()
    calculator.characters_no_spaces()

    calculator.character_counter()
    calculator.word_counter()
    calculator.average_word_length()
    
    # JSON or pickle writer
    calculator.writer()
        
main()

#:#:#:# - - - - - - - - - ! 2 DO !
"""
- daten in pickle oder json file schreiben lassen
-tkinter
"""
