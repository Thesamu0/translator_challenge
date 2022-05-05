# Storing utility methods that will be used elsewhere in the code

def get_key(val,dict):
    for key,value in dict.items():
        if val == value:
            return key
    
    return None

def morse_to_text(mystr):
    morse_dictionary = {
        '.-':'a',
        '-...':'b',
        '-.-.':'c',
        '-..':'d',
        '.': 'e',
        '..-.': 'f',
        '--.':'g',
        '....':'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        ' ': ' '
    }
    splitstr = mystr.split('/')
    translated_str = ''
    for morse_char in splitstr:
        if morse_dictionary.get(morse_char) is not None:
            translated_str += (morse_dictionary.get(morse_char))
        else:
            return "Error - Invalid char detected in string"
    
    return translated_str

def text_to_morse(mystr):
    morse_dictionary = {
        '.-':'a',
        '-...':'b',
        '-.-.':'c',
        '-..':'d',
        '.': 'e',
        '..-.': 'f',
        '--.':'g',
        '....':'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        ' ': ' '
    }
    translated_str = ''

    for char in mystr:
        if get_key(char,morse_dictionary) is not None:
            translated_str += get_key(char,morse_dictionary)
            translated_str += '/'
        else:
            return "Error - Invalid char detected in string"
    
    return translated_str