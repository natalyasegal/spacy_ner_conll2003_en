# spacy_ner_conll2003_en
##The project contain the following notebooks:

- parse_data.ipynb - heavy notebook, it's results are stored in data directory, so that you can start from the explore_data.ipynb
- explore_data.ipynb - lighweight notebook with data exploration
- train_ner_spacy_conll2003.ipynb - can train on CPU in reasonable time

note: please set your Jupiter working directory to <...your path>/ner_proj/notebooks, can be done by running: jupyter notebook --notebook-dir=/<...your path>/ner_proj/notebooks


## Steps to create docker container and run it (ner_spacy_ns is a container name, you can change it):
- cd ner_proj/docker_ns
- docker build -t ner_spacy_ns .
- docker run -it ner_spacy_ns

