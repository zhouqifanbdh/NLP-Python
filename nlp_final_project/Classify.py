from cluster import read_txt, cut_doc
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def create_dataset(path):
    doc_df = read_txt(path)
    cut_df = cut_doc(doc_df)
    doc = [' '.join(x) for x in cut_df['cut_doc']]
    vectorizer = TfidfVectorizer(use_idf=True)
    tfidf = vectorizer.fit_transform(doc).toarray()
    return tfidf, cut_df['label'].values

if __name__ == "__main__":
    path = './data'
    X, y = create_dataset(path)
    x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.75)
    knn = KNeighborsClassifier(5)
    knn.fit(x_train, y_train)
    print('Training Score: {}'.format(knn.score(x_train,y_train)))
    print('Testing Score: {}'.format(knn.score(x_test, y_test)))
