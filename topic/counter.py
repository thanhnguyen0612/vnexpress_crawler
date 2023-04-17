import re
import os
import glob

outputDir = "output"
frequency = {}
# document_text = open('test.txt', 'r')
# text_string = document_text.read().lower()
# match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
# for word in match_pattern:
#     count = frequency.get(word,0)
#     frequency[word] = count + 1
    
# frequency_list = frequency.keys()
# for words in frequency_list:
#     print(words, frequency[words])

def countWordsFrequency():
    if os.path.exists(outputDir):
        files = glob.glob(outputDir + "/*.txt")
        for file in files:
            document_text = open(file, 'r')
            text_string = document_text.read().lower()
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
            for word in match_pattern:
                count = frequency.get(word,0)
                frequency[word] = count + 1
                
            frequency_list = frequency.keys()
            for words in frequency_list:
                print(words, frequency[words])



