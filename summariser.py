# Import required libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

class Summarizerr():

    def __init__(self, url):
        self.url = url

    def articleSummary(text, num_sentences=5):
        # Load the pre-trained NLP model
        nlp = spacy.load('en_core_web_sm')

        # Initialize English tokenizer
        #tokenizer = English().Defaults.create_tokenizer(nlp)
        
        # Parse the input text
        doc = nlp(text)

        # Calculate the token scores using TextRank algorithm
        scores = {}
        for sent in doc.sents:
            for token in sent:
                if token.text.lower() not in STOP_WORDS and not token.is_punct:
                    if token.text not in scores.keys():
                        scores[token.text] = token.similarity(doc)

        # Sort the sentences based on their scores
        sorted_sents = sorted(doc.sents, key=lambda sent: sum([scores[token.text] for token in sent if token.text in scores.keys()]), reverse=True)

        # Return the top `num_sentences` sentences as the summary
        summary = ''
        for sent in sorted_sents[:num_sentences]:
            summary += sent.text.strip() + ' '

            return summary

            