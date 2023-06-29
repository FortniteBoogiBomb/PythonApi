from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model
my_model = load('lin_model.pkl')
class_names = NN['Overall', 'PTS']

def my_prediction(id):
  dummy = np.array(id)
  dummyT = dummy.reshape(1,-1)
  r = dummy.shape
  t = dummyT.shape
  r_str = json.dumps(r)
  t_str = json.dumps(t)
  prediction = Trained_Model.predict(dummyT)
  name = class_names[prediction]
  name = name.tolist()
  name_str = json.dumps(name)
  str = [t_str, r_str, name_str]
  return str
