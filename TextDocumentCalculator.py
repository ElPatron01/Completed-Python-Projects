""" Implementation of a calculator which takes statistics about a given file"""

__author__ = "6598477: Jannik Zorn, 6586227: Eric J. Herschbach"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__email__ = "<Jannik@zorn.net>, <Eric.Herschbach@t-online.de>"

file_to_read = input("Enter the name of the file you want to have statistics about: ")

# - - - - - - - - - - - - - - - - - - CLASS/METHODS
class Statistics:

    def __init__(self):
        """Opens the existing txt-file and save it in variable"""
        self.file = open(file_to_read, encoding = "utf-8")
        self.lines = self.file.readlines()
        self.amount_words = ''.join(self.lines)
        self.amount_characters = ''.join(self.amount_words.split()) 
        self.amount_characters2 = ''.join(self.amount_words)

    def print_txt(self):
        """Prints the whole text into console"""
        for data in self.lines:
            print(data)

    def amount_of_words(self):
        """Shows the amount of all words in the file"""
        print("The amount of words in the file: ", len(self.amount_words.split()))

    def amount_lines(self):
        """Shows the amount of all lines in the file"""
        print("The amount of lines in text: ", len(self.amount_words.splitlines()))

    def amount_no_whitespace(self):
        """Shows the amount of characters without spaces"""
        print("The amount of characters in text: ", len(self.amount_characters))

    def average_length(self):
        """Shows average word length"""
        print("The average word length: ", len(self.amount_characters)/len(self.amount_words.split()))

    def average_characters(self):
        """Shows the average characters in line"""
        print("The average of characters (in each line): ",
              len(self.amount_characters2)/len(self.amount_words.splitlines()))

    def average_words_in_line(self):
        """Shows the average amount of words in a line"""
        print("Average of words (in each line): ", len(self.amount_words.split())/len(self.amount_words.splitlines()))

# - - - - - - - - - - - - - - - - - - MAIN FUNCTION 
def main():
    statistics = Statistics()
    statistics.print_txt()
    statistics.amount_of_words()
    statistics.amount_lines()
    statistics.amount_no_whitespace()
    statistics.average_length()
    statistics.average_characters()
    statistics.average_words_in_line()
    
main() 


