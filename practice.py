

#define the function

def LongestWord(sen):
    current_word = ''
    longest_word = ''
    
    for char in sen:
      
        if char.isalnum():
          
           current_word += char
        else:
            if len(current_word) > len(longest_word):
               longest_word = current_word
               
               current_word = ''
      
    if len(current_word) > len(longest_word):
        longest_word = current_word
    return longest_word
  
print(LongestWord("jeff habakuk"))                
    