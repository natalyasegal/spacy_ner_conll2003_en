import spacy

nlp = spacy.load("/app/en_model-0.0.0/en_model/en_model-0.0.0/")
doc = nlp(u'Ronald just bought 2 shares at 9 a.m. because the stock went up 30% in just 2 days according to the WSJ. Us is a country in north America')
for ent in doc.ents:
    print(ent.text, ent.label_)