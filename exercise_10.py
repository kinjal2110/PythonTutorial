#Machine Leaning Repository
# use of request module and pickle.

#internet connection are required for run.++
import pickle
import requests
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
respons = requests.get(url)
res_text = respons.text
data = res_text.splitlines()
red = [[i] for i in data]

# pickling the python object.
fileobj = open("irisData.pkl", "wb")
pickle.dump(red, fileobj)
fileobj.close()

#reading of pickle file
fileobj = open("irisData.pkl", "rb")
data = pickle.load(fileobj)
print(data)