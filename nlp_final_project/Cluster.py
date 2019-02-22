import os
import pandas as pd
import jieba.analyse
import gensim
from gensim.models import LdaModel, TfidfModel

def read_txt(path):
    txt_list = os.listdir(path)
    doc = []
    label = [i.split('_')[0] for i in txt_list]
    for txt in txt_list:
        with open(path + '\\' + txt, 'r') as f:
            doc.append(''.join(f.readlines()))
    doc_df = pd.DataFrame({'doc':doc, 'label':label})
    return doc_df

def cut_doc(doc_df):
    jieba.analyse.set_stop_words('.\stopwords_zh.txt')
    cut_doc = [jieba.analyse.extract_tags(txt) for txt in doc_df['doc']]
    return pd.DataFrame({'cut_doc':cut_doc, 'label':doc_df['label']})


def lda_model(cut_df, num_topics=10, top_words = 5, show=True):
    te = cut_df['cut_doc'].values
    dictionary = gensim.corpora.Dictionary(te)
    corpus = [dictionary.doc2bow(text) for text in te]
    #corpus -> tfidf
    tfidf = TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    #tfidf -> lda
    lda = LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=num_topics)
    corpus_lda = lda[corpus]
    if show:
        topics = lda.print_topics(num_topics, top_words)
        for toc in topics:
            print(toc)
    return lda

if __name__ == "__main__":
    path = '.\data'
    doc_df = read_txt(path)
    #分词
    cut_df = cut_doc(doc_df)
    #LDA
    lda = lda_model(cut_df, num_topics=10, top_words=5, show=True)

