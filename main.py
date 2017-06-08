import urllib
import zipfile
import nottingham_util
import rnn

# collect the data
# url = "http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
# urllib.urlretrieve(url, "dataset.zip")

zip = zipfile.ZipFile(r'dataset.zip')
zip.extractall('data')

# build the model
print "Creating model..."
nottingham_util.create_model()

# train the model
print "Training model..."
rnn.train_model()
