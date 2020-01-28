import fasttext
import jieba
from constant import STOPWORDS
import re


def get_model_api():
    model = fasttext.load_model("fasttext.model")

    def model_api(input_data):
        query = preprocessed_text(input_data)
        preds_label = model.predict(query)
        print(preds_label)
        LABEL_2_CATE = {"__label__1": 'technology',
                        "__label__2": 'car',
                        "__label__3": 'entertainment',
                        "__label__4": 'military',
                        "__label__5": 'sports'}
        output = LABEL_2_CATE[str(preds_label[0][0])]
        return output

    def preprocessed_text(text):
        segs = jieba.lcut(re.sub("\n", "", text))
        segs = list(filter(lambda x: len(x) > 1, segs))
        segs = list(filter(lambda x: x not in STOPWORDS, segs))
        return " ".join(segs)

    return model_api
