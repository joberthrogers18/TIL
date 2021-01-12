import re
import requests
the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def get_book(url):
    # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Discards the metadata from the beginning of the book
    start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*",raw ).end()
    # Discards the text starting Part 2 of the book
    stop = re.search(r"II", raw).start()
    # Keeps the relevant text
    text = raw[start:stop]
    return text

def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()

if __name__ == "__main__":
    book = get_book(the_idiot_url)
    
    processed_book = preprocess(book)
    
    # get all the pronouns "the" in capther
    print("Counting of pronouns 'The':", len(re.findall(r'the', processed_book)))
    # change i lowercase to I uppercase when it alone
    print(re.sub(r'\si\s', r'\sI\s', processed_book))