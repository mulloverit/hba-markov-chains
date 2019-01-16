"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

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
    
    # establish empty dict to be populated with chains from incoming corpus
    chains = {}

    # split corpus by whitepace, including new lines
    words = text_string.split()

    # loop over indices the length of corpus, minus two positons
    # use -2 because the length of desired chain is 2 and positions 
    # for terminal chain must be ignored to avoid infinite chaining
    for idx in range(len(words) - 2):
    
        # while looping over corpus, take each word & it's following neighbor
        # add the pair to chains dict as tuple & make their value an empty list
        chains[(words[idx], words[idx + 1])] = []


    # now that dict keys are populated with tuples,
    # loop over all dict items to begin populating values
    for key_pair, value_list in chains.items():
        
        # iterate over each index & word in the split list version of corpus
        for idx, word in enumerate(words[:-2]):
            
            # where a word & it's trailing neighbor are equal to dict key
            # add the trailing neighbor of pair (idx + 2) to the list value of key
            if (key_pair) ==  (words[idx], words[idx + 1]):
                value_list.append(words[idx + 2])
    
    # return populated dictionary             
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # get any key in dict, then get one of that key's values randomly
    # store that key/value pair into another list
    # join that list into a string
    # use key[1] + value as new key, and get next random value
    # repeat until KeyError

    values = choice(chains.keys())
    print(values)
    tuples = chains.keys()
    #text_from_chains = choice(tuples) + choice(values)
    #print(text_from_chains)
    # # 
    # #chains.get

    #return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
