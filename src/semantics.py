import nltk

nltk.download("omw")
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

def get_hyponyms(synsets):
    synset = synsets[0]
    
    hyponyms = []
    
    for hyponym in synset.hyponyms():
        hyponyms.extend(hyponym.lemma_names('por'))
        
    return hyponyms

def get_hypernyms(synsets):
    synset = synsets[0]
    
    return synset.hypernyms()[0].lemma_names('por')

def get_synonyms(synsets):
    synset = synsets[0]
    
    return synset.lemma_names('por')

def search_wordnet(searched_word):
    synsets = wn.synsets(searched_word, lang='por')

    data = {
        'searched_word': searched_word,
        'synonyms': get_synonyms(synsets),
        'hypernyms': get_hypernyms(synsets),
        'hyponyms': get_hyponyms(synsets)
    }
    
    return data