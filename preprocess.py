import string, sys


stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
"yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
"hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
"themselves", "what", "which","who", "whom", "this", "that", "these", "those", 
"am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had", 
"having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if", 
"or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
"about", "against", "between", "into", "through", "during", "before", "after", 
"above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
"under", "again", "further", "then", "once", "here", "there", "when", "where", 
"why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
"some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def rem_punc(list_in):
    """ Removes punctuation in all strings of a list

    Arguments:
        list_in (list): A list containing strings

    Returns:
        out (list): Output list that stores processed words
    """
    out = []
    for i in list_in:
        letters = []
        for j in i:
            if j not in string.punctuation:
                letters.append(j)
        words = ''.join(letters)
        out.append(words)
    return out

def rem_numbers(list_in):
    """ Removes numbers from words only if the string is not
    entirely numbers

    Arguments:
        list_in (list): A list containing strings

    Returns:
        out (list): Output list of strings from list_in with 
                    numbers selectively removed
    """
    out_list = []
    for i in list_in:
        word = []
        if not i.isdigit():
            for letter in i:
                if not letter.isdigit():
                    word.append(letter)
            word = "".join(word)
            out_list.append(word)
        else:
            out_list.append(i)
    return out_list

def rem_stop(list_in, stop_list=stopwords):
    """ Removes all the words in a list that appear in the `stopwords`
    list.

    Arguments:
        list_in (list): A list of strings 
        stop_list (list): A list containing strings that will be removed
                        from list_in

    Returns: 
        out (list): Output list of strings of list_in, but with elements
                    that are in stop_list removed.
    """
    out = []
    for i in list_in:
        if i not in stop_list:
            out.append(i)
    return out

def handle_cmd_line():
    """ Handles command line arguments, which changes the default configs
    stored in init_vars dictionary.

    Returns:
        init_vars (dict): a dictionary of the starting values of keep-symbols, 
                            keep-digits, and keep-stops, which by default are 
                            False. If command line arguments are passed through, 
                            then the values of init_vars will be changed and then
                            returned.
    """
    init_vars = {
        "keep-digits": False,
        "keep-stops": False,
        "keep-symbols": False
    }
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "keep-digits":
            init_vars["keep-digits"] = True
        elif sys.argv[i] == "keep-stops":
            init_vars["keep-stops"] = True
        elif sys.argv[i] == "keep-symbols":
            init_vars["keep-symbols"] = True
        else:
            print("Error: faulty arguments")
            print("Usage: \n    python3 preprocess.py [option 1] [option 2] [option 3]")
            print("    [options] : keep-digits, keep-symbols, keep-stops")
            sys.exit()
    return init_vars


def main():


    init_dict = handle_cmd_line()

    x = input().lower().split()
    if not init_dict["keep-symbols"]:
        x = rem_punc(x)
    if not init_dict["keep-digits"]:
        x = rem_numbers(x)
    if not init_dict["keep-stops"]:
        x = rem_stop(x)
    print(" ".join(x))


if __name__ == "__main__":
    main()
