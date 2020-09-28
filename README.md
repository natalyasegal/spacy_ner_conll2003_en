# spacy_ner_conll2003_en
### The project contain the following notebooks:

- parse_data.ipynb - heavy notebook, it's results are stored in data directory, so that you can start from the explore_data.ipynb
- explore_data.ipynb - lighweight notebook with data exploration
- train_ner_spacy_conll2003.ipynb - can train on CPU in reasonable time

note: please set your Jupiter working directory to <...your path>/ner_proj/notebooks, can be done by running: jupyter notebook --notebook-dir=/<...your path>/ner_proj/notebooks


## Steps to create docker container and run it (ner_spacy_ns is a container name, you can change it):
- cd ner_proj/docker_ns
- docker build -t ner_spacy_ns .
- docker run -d -p 5000:5000 -it ner_spacy_ns

## To run inference example (or same url from browser):
- curl http://0.0.0.0:5000/example

## To run NER on your text from the command line 
- place you text after the =, like in example below. 
curl http://0.0.0.0:5000/inp_text=Daniel%20is%20travelling%20to%20US

## To run from browser 
- open a browser and go to url: http://0.0.0.0:5000/inp_text=you text without ecape characters



## If you need to stop and remove other containers that take the ports above:
- docker ps
- docker stop container_id
- docker rm  container_id

## If there any problem and you'd like to view cintainer logs 
- note: container_id is taken from docker ps
- docker logs container_id
