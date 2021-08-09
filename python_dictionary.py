# understanding python dictionary
from pprint import pprint
def does_sent_term_hit(terms, sentences):
    """gives you the list of terms hit and the sentences
    
    Args:
        terms (list): list of terms
        sentences (list): sentences list to match against terms
    """
    sentence_dict = {}
    sentence_dict["sentences"] = sentences
    sentence_dict['terms'] = []
    for term in terms:
        for sentence in sentence_dict["sentences"]:
            if term.lower() in sentence.lower():
                sentence_dict["terms"].append(term) 
    pprint(sentence_dict)


terms_list = ['shweata', 'shamanta', 'hockey']
sentences_list = ['shweata is learning to code',
                    'shweata likes badminton',
                    'shamanta loves chocolate']

does_sent_term_hit(terms_list, sentences_list)