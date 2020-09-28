# input: 
#    filename of the train, validation and test fines to parse
# output: 
#    df_freq dataframe with columns representing token, pos, chunk, lable, example: LEICESTERSHIRE NNP B-NP B-ORG
#    df_features - dataframe with 2 columns: features list and lables list, 
#                  example: Features: [“Jacob”, “went”,”to”,”Paris”], Labels: [“B-PER”, “O”, “O”, “B-LOC”]

import pandas as pd


def create_df(filename):
    df_freq = pd.DataFrame(columns=('token', 'pos', 'chunk', 'lable'))
    df_features = pd.DataFrame(columns=('features', 'lables'))
    
    try:
        f = open(filename, "r")
    except: 
        print('Unable to open an input file ' + filename)
    else:
        j = 0
        list_features = []
        list_lables = []
        try:
            f.readline()
            for i, x in enumerate(f):
                vals = x.split()
                if len(vals) > 0:
					# record entries per individual token, in format: 'token', 'pos', 'chunk', 'lable'
                    df_freq.loc[i-1] = vals
                    list_features.append(vals[0])
                    list_lables.append(vals[3])
                else:
                    if len(list_features) > 1 or len(list_features) == 1 and list_features[0] != "-DOCSTART-":
						# record samples, each sample is a sentence, format: [tokens], [lables]
                        df_features.loc[j] = [list_features, list_lables]
                        j = j + 1
                        if(j % 50 == 0):
                        	print('progres: formatted ', j ,'sentences in ', filename)
                    list_features = []
                    list_lables = []
        except:
             print('error reading from input file' + filename)
        finally:
            f.close()
    return df_freq, df_features
	
	
def test_create_df():
	pass
	#in a real life project here will be tests main and of edje cases, as we have a linited time 
	#for the challenge I tested in the notebook and then remove the tests