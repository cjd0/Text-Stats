import re

class Text_Stats(object):
    
    def text_stats(self, text):
        """
        :type text: string
        :rtype: string
        """

        #number of characters
        char_count = str(len(text))

        
        #initialise count variables
        vowel_count = 0
        consonant_count = 0
        letter_count = 0
        digit_count = 0
        punctuation_count = 0
        word_count = 0
        non_space_count = 0
        avg_word_length = 0        
        
        #define regex patterns and compile each once for more efficient character analysis
        #also account for accented latin alphabet letters
        vowel_pattern = re.compile(r'[aeiouáéíóúAEIOUÁÉÍÓÚàèìòùÀÈÌÒÙäëïöüÄËÏÖÜ]')
        consonant_pattern = re.compile(r'[bcčçdfgġhjklłmnňpqrsštŧvwxyzźżBCČÇDFGĠHJKLŁMNŇPQRSŠTŦVWXYZŹŻ]')
        digit_pattern = re.compile(r'[0123456789]')

        #count first word if text is not empty and contains letters
        if len(text) > 0:
            if vowel_pattern.search(text) or consonant_pattern.search(text):
                word_count = 1

        for i in text:
            
            #count each space as long as it is not preceded by a space and is not the first character
            if i == " " and text[text.index(i)-1] != " " and text.index(i) != 0:
                word_count += 1

            #vowel/consonant/letter/digit/punctuation counts
            if vowel_pattern.match(i):
                vowel_count += 1
                letter_count += 1
            elif consonant_pattern.match(i):
                consonant_count += 1
                letter_count += 1
            elif digit_pattern.match(i):
                digit_count += 1
            else:
                punctuation_count += 1


            #count all non whitespace characters to calculate average word length
            if i != " ":
                non_space_count += 1

            
        #check to prevent division by 0
        if word_count > 0:
            avg_word_length = str(float(non_space_count/word_count))
        
        return (f"Character count: {char_count}\nWord count: {str(word_count)}\nVowel count: {str(vowel_count)}\nConsonant count: {str(consonant_count)}\n" 
                + f"Letter count: {letter_count}\nDigit count: {digit_count}\nPunctuation count: {punctuation_count}\n" 
                + f"Average word length: {avg_word_length}")


text_stats_instance = Text_Stats()

input_text = input("Please enter the text to be evaluated: ")

result = text_stats_instance.text_stats(input_text)
print(result)