# project 2 challenge

# def main():

#     replace = input("Input: ")
#     print("Output: ", end="")
   
#     for letter in replace:
#         if not letter.lower() in ["a", "e", "i", "o", "u"]:
#             print(letter, end="")
    
#     print()

# if __name__ == '__main__':
#     main()


def main():
        message = input("Input: ")
        message_no_vowels = shorten(message)
        print("Output:" + message_no_vowels)

def shorten(word):
        word_no_vowels = ""
        for letter in word:
                if not letter.lower() in ["a", "e", "i", "o", "u"]:
                        word_no_vowels += letter
        return word_no_vowels

if __name__ == '__main__':
        main()