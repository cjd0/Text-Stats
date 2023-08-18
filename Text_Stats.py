import re

class Text_Stats(object):
    
    def text_stats(self, text):
        """
        :type text: string
        :rtype: string
        """

        char_count = str(len(text))

        #used for average word length calculation
        non_space_count = 0

        #do not let this be a permanent solution!
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
               
        vowel_count = 0
        consonant_count = 0

        #count first word if text is not empty and contains letters
        if len(text) > 0 and re.search('[a-zA-Z]', text):
            word_count = 1
        else:
            word_count = 0

        for i in text:
            
            #count each space as long as it is not preceded by a space and is not the first character
            if i == " " and text[text.index(i)-1] != " " and text.index(i) != 0:
                word_count += 1

            if i in vowels:
                vowel_count += 1

            if i in consonants:
                consonant_count += 1

            if i != " ":
                non_space_count += 1


        return ("Character count: " + char_count + "\nWord count: " + str(word_count) + "\nVowel count: " + str(vowel_count) + "\nConsonant count: " + str(consonant_count) + 
                "\nAverage word length: " + str(float(non_space_count/word_count)))


text_stats_instance = Text_Stats()

input_text = input("Please enter the text to be evaluated: ")

result = text_stats_instance.text_stats(input_text)
print(result)