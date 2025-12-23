# def LongestWord(sen):
#     current_word = ''
#     longest_word = ''
    
#     for char in sen:
      
#         if char.isalnum():
#             current_word += char
            
#         else:
#             if len(current_word) > len(longest_word):
#                 longest_word = current_word
            
#             current_word = ''
#     if len(current_word) > len(longest_word): 
#         longest_word = current_word
#     return longest_word
# print(LongestWord("Python3.10 is awesome, but JavaScript42 is fun too!"))                    


def LongestWord(sen):
    valid_char = ''
    
    for char in sen:
       if char.isalnum():
           valid_char += char
       else:
           valid_char += ' '
           
    words = valid_char.split()
    
    return max(words,key=len)       
        
print(LongestWord("Python3.10 is awesome!"))            