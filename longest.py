"""
Task:
Write a function that returns the longest word in the sentence below.
A word is made up of letters and numbers only (ignore symbols and punctuation).

Sentence to use:
"Hello!!! this_is a t3sting sentence, with longestWord123 inside."
"""
# defining the function
def LongestWord(sen):
    current_word = ''
    longest_word = ''
    #itarating through the sentence 
    for char in sen :
      #checks if the char is alphabetic or numeric and continues building if the condition it true.
        if char.isalnum():
            current_word += char
        else:
            if len(current_word) > len(longest_word):
                longest_word = current_word 
            
            current_word = ''   

    if len(current_word) > len(longest_word):
        longest_word = current_word
        
    return longest_word
  
  
print(LongestWord("Hello!!! this_is a t3sting sentence, with longestWord123 inside."))                  