from transformers import BertForMaskedLM, BertTokenizer

class LanguageModel:
    def __init__(self, model_name):
        print("Download language model...")
        self.__tokenizer = BertTokenizer.from_pretrained(model_name)
        self.__model = BertForMaskedLM.from_pretrained(model_name, return_dict=True)
    
    def initTokenizer(self):
        return self.__tokenizer
    
    def initModel(self):
        return self.__model