from gensim.models import Word2Vec

import hyperparameters_pytorch as hparams
import numpy as np

def WordEmbedding(sentences, save=False):
    model = Word2Vec(sentences=sentences, size=hparams.d_model, window=4, min_count=1, workers=4)
    if save:
        model.save("word2vec.model")
    return model

def Custom_WordEmbedding(sentences):
    src_sentences = []
    trg_sentences = []
    length = len(sentences.examples)
    for i, obj in enumerate(sentences.examples):
        src_sentences.append(obj[i].src)
        trg_sentences.append(obj[i].trg)
        print(i, length, sep='/')
    np.hstack(src_sentences, trg_sentences)
    src_model = Word2Vec(sentences=src_sentences, size=hparams.d_model, window=4, min_count=1, workers=4)
    trg_model = Word2Vec(sentences=trg_sentences, size=hparams.d_model, window=4, min_count=1, workers=4)

    src_model.save("src_model.model")
    trg_model.save("trg_model.model")

    return src_model, trg_model