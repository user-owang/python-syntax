def print_upper_words(words):
    """Given list of words, print each word in all caps.

    For example:
      print_upper_words(['yo','gabba','gabba'])

    Should print (not return)):
      YO
      GABBA
      GABBA
    """  
    # YOUR CODE HERE
    for word in words:
        print(word.upper())


print_upper_words(['yo','gabba','gabba'])
