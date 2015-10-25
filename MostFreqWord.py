import re

def checkio(text):
    most_freq_alpha = None
    max_letter_freq = 0
    
    clean_txt = ('').join(re.findall(r'[a-zA-W]+', text)).lower()
    
    for alpha in clean_txt:
        if (clean_txt.count(alpha) > max_letter_freq or 
            (clean_txt.count(alpha) == max_letter_freq and alpha > most_freq_alpha)):
                most_freq_alpha = alpha
                max_letter_freq = clean_txt.count(alpha)
    
    return most_freq_alpha

print(checkio("Hello World!"))
