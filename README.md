Overview
============
A project that trains a LSTM recurrent neural network over a dataset of MIDI files. More information can be found on the [writeup about this project](http://yoavz.com/music_rnn/). This the code for 'Build an AI Composer' on [Youtube](https://youtu.be/S_f2qV2_U00)

Dependencies
============

* Numpy (http://www.numpy.org/)
* Tensorflow (https://github.com/tensorflow/tensorflow)
* Python-Midi (https://github.com/vishnubob/python-midi.git)
* Mingus (https://github.com/bspaans/python-mingus)

Use [pip](https://pypi.python.org/pypi/pip) to install any missing dependencies

Installation (Tested on Ubuntu 16.04)
============

* Step 1: Tensorflow version 1.1.0 must be used. On [Tensorflow's download page here](https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html).

* Step 2: After installing Tensorflow, you will have to install the missing dependencies(choose what you need to install):

  `sudo pip install matplotlib`

  `sudo apt-get install python-tk `

  `sudo pip install numpy`

  `sudo pip install pyhton-midi`

  `sudo pip install mingus`


Basic Usage
===========

1. `mkdir data && mkdir models`
2. run `python main.py`. This will collect the data, create the chord mapping file in data/nottingham.pickle, and train the model
3. Run `python rnn_sample.py --config_file <path/to/new_config_file.config>` to generate a new MIDI song.

Give it 1-2 hours to train on your local machine (it seems 100 epoches is good enough), then generate the new song. You don't have to wait for it to finish, just wait until you see the `saving model` message in terminal. You can convert the midi file into mp3 using the online converter [here](http://www.conversion-tool.com/midi)

Credits
===========
Credit for the vast majority of code here goes to [Yoav Zimmerman](https://github.com/yoavz). I've merely created a wrapper around all of the important functions to get people started.
