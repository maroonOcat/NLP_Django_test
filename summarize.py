import get_text
import spacy
import pytextrank
from spacy.lang.ru.examples import sentences
from spacy.lang.ru import Russian


# Print the text
text_content = get_text.get_text("pdf_text.pdf")
print(text_content)

nlp = Russian()
nlp = spacy.load("ru_core_news_sm")
nlp.add_pipe("textrank")

doc = nlp(text_content)
print(text_content)
print('Original Document Size:',len(text_content))

text_summary = ""
for sent in doc._.textrank.summary(limit_phrases=2, limit_sentences=2):
    text_summary += str(sent)
    print(sent)
    print('Summary Length:',len(sent))