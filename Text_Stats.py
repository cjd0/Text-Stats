import re

class Text_Stats(object):
    
    def text_stats(self, text):
        """
        :type text: string
        :rtype: string
        """

        char_count = str(len(text))
               

        #count first word if text is not empty and contains letters
        if len(text) > 0 and re.search('[a-zA-Z]', text):
            word_count = 1
        else:
            word_count = 0

        for i in text:
            
            #count each space as long as it is not preceded by a space and is not the first character
            if i == " " and text[text.index(i)-1] != " " and text.index(i) != 0:
                word_count += 1

        return "Character count: " + char_count + "\n Word count: " + str(word_count)


text_stats_instance = Text_Stats()

input_text = input("Please enter the text to be evaluated: ")

result = text_stats_instance.text_stats(input_text)
print(result)