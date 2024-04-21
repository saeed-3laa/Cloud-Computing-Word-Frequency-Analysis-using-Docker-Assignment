import re
from collections import Counter
from nltk.corpus import stopwords  
import nltk

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_word_frequency(words_list):
    word_counts = Counter(words_list)
    return word_counts

def main():
    nltk.download('stopwords')

    file_path = 'random_paragraphs.txt'
    with open(file_path, 'r') as file:
        text = file.read()

    processed_text = remove_stopwords(text)

    word_frequency = count_word_frequency(processed_text)

    for word, count in word_frequency.items():
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()
