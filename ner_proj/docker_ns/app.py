# library to be used for inference
import spacy

# library that we need for rpc
from flask import Flask
server = Flask(__name__)

nlp = spacy.load("/app/en_model-0.0.0/en_model/en_model-0.0.0/")

def ner_inference(doc):
	res = ""
	for ent in doc.ents:
		res = res + ent.text + " " + ent.label_ + "\n"
	res = res + "\n"
	return res
	
@server.route('/<string:inp_text>')
def request_with_params(inp_text = None):
	if inp_text == None:
		return "Please provide input text!"
	
	doc = nlp(inp_text)
	return ner_inference(doc)
	
@server.route('/example')
def example():
	doc = nlp(u'Ronald just bought 2 shares at 9 a.m. because the stock went up 30% in just 2 days according to the WSJ. Us is a country in north America')
	return ner_inference(doc)
		
if __name__ == "__main__":
	server.run(host='0.0.0.0')