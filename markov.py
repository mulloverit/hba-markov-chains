"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    full_text = open(file_path).read()

    return full_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    # split the incoming text at spaces
    # use a for loop to pair words into tuples - overlapping
    # ignore last word? pair? in text block
    # create dictionary with tuples as keys
    # look in text block for each tuple to get the words that follow it to add 
    # list of keys

    words = text_string.split()

    for i in range(len(words) - 2):
        # take var of tuple and shovel into dict as a key
        
        # alternative solution, potentially superior for readability?
        # pair = (words[i], words[i + 1])
        # chains[pair] = []
        
        chains[(words[i], words[i + 1])] = []

    # dictionary, look at the word set in our tuple and find the following word(s)
    # in text_string and add to list each time it appears 
    # actions:  crawling text looking for tuples
    #           updating dict with new values in list form
    # for each key in text_string, if it follows the tuple pair, add to list
    for key_pair, value_list in chains.items():
        
        # print(key_pair)
        # print(value_list)

        # look for key in text
        # append following word to value

        # in words, every time you have occurent of tuple, take +1 
        

        # need to have index of tuple occurence, take the second word's index
        # add one to that index 
        for idx, i in enumerate(words[:-2]):
            
            #print((words[idx] + " " + words[idx + 1]))
            if (key_pair) ==  (words[idx], words[idx + 1]):
                value_list.append(words[idx + 2])
        
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
