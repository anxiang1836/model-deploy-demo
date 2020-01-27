import pandas as pd

stopwords = pd.read_csv("origin_data/stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                         encoding='utf-8')
STOPWORDS = stopwords['stopword'].values


