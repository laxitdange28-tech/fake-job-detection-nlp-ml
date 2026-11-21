import re
import html
import nltk

from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


# NLTK data location
nltk.data.path.append("/home/codespace/nltk_data")


# Initialize NLP tools
lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))
stop_words = stop_words - {"no", "not", "nor"}


# Convert POS tags into WordNet POS
def get_wordnet_pos(tag):

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    else:
        return wordnet.NOUN


# Basic text cleaning
def clean_text(text):

    text = html.unescape(text)

    text = re.sub(r"http\S+|www\S+", " ", text)

    text = re.sub(r"#URL_[^#]*#", " ", text)

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# Complete NLP preprocessing
def preprocess_text(text):

    if not isinstance(text, str):
        return ""

    text = clean_text(text)

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word.isalpha() and word not in stop_words
    ]

    tagged_words = pos_tag(tokens)

    processed_words = []

    for word, tag in tagged_words:

        pos = get_wordnet_pos(tag)

        lemma = lemmatizer.lemmatize(word, pos)

        processed_words.append(lemma)

    return " ".join(processed_words)