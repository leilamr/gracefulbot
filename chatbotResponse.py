#imports
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import random

#restaura as estruturas de dados
import pickle
data= pickle.load(open("training_data", "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

#importa o intens.json
import json
with open('intents.json') as json_data:
    intents = json.load(json_data)

#construçao da rede neural
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

def cleanup_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

#return 0 ou 1 para cada palavra no pacote de palavras que existir na sentença
def bow(sentence, words, show_details=False):
    sentence_words = cleanup_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
            for i,w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("encontrada no pacote: %s" % w)


    return (np.array(bag))

#teste pequeno
#p = bow("voce vai ter um bom dia hoje se for grata?", words)
#print(p)
#print(classes)

#carrega modelo definido no arquivo: chatbot-tf-model
model.load('./model.tflearn')

#cria uma ed para manter o contexto do user
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    results = model.predict([bow(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    if results:
        while results:
            for i in intents['intents']:
                if i['tag'] == results[0][0]:
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details:
                            print ('tag:', i['tag'])
                        msg = random.choice(i['responses']) +" \n\n(Classificação: "+i['tag']+")"
                        return msg


            results.pop(0)


