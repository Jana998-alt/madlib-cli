import re
# welcome message

def welcome_mss():
    print("Hey there! \nwelcome to madlib game! \nI will ask you a series of quistions, and I\ll ask you to answer them according to the instructions, the result will be something fun, I promise. \n let\'s get started....")
    

# read & parse file

def  read_template(file):
    try:
        file_opened = open(file, 'r')  
        file_text = file_opened.read()
    except FileNotFoundError:
        file_text = 'file not found'
        raise FileNotFoundError
    else:
        file_opened.close()
    return file_text


def parse_template(string_to_parse):
    stripped = re.sub('\{.*?\}',  '{}', string_to_parse)  
    parts = re.findall('(?<=\{).+?(?=\})', string_to_parse)
    return (stripped, tuple(parts))


def merge(string_to_merge, list_of_words):
    return string_to_merge.format(*list_of_words)

# prompt input sequence  

def prompt_sequence_of_variables():
    pass

# - prompt with answer  

def prompt_result_text():
    pass

#  write the result in a new file
def write_result_in_file():
    pass

if __name__ == "__main__":
    welcome_mss()
    text_from_file = read_template('./assets/dark_and_stormy_night_template.txt')
    parse_template(text_from_file)