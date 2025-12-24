#Palindrome
#Reverse in action

# def is_palindrome(word):
#     #reverse action
    
#     reversed_word = word[::-1]
#     #compare them
#     if word == reversed_word:
#         return True
      
#     else:
#         return False  
    
# print(is_palindrome("cat"))
# print(is_palindrome("mom"))
# print(is_palindrome("egg"))


# solving palindrome with spaces and symbols

# def is_palindrome(word):
#     #clean the strings (spaces & symbols)
#     clean_word = ''
    
    
#     #loop through every character
#     for char in word:
#         #check if a latter or a number(ignore spaces/symbols)
#         if char.isalnum():
#             # add it to our clean string(make it lowercase)
#             clean_word += char.lower()
            
#     #compare with the reverse
#     return clean_word == clean_word[::-1] 
  
# print(is_palindrome('Taco Cat!'))         
# print(is_palindrome('Regan Saf!')) 


#senior solution (Two Pointers)
def is_palindrome_optimized(word):
    left = 0
    right = len(word) -1  
    
    while left < right:
      #move left pointer forward if it's not a letter/number
        if not word[left].isalnum():
            left  += 1
            #skip to next loop iteration
            continue
         #move right pointer backward if it's not a letter/number 
        if not word[right].isalnum():
            right -= 1
            
            continue 
        
        if word[left].lower() != word[right].lower():
            return False
          
        left += 1
        right -= 1 
        
    return True  
  
print(is_palindrome_optimized("Taco Cat!"))           
    
    

