# Virality Predictor
The project consists of a model that can predict whether a given tweet will be viral or not. For model training, the dataset is prepared by web scrapping using tweepy API in python.  In addition to that, through web crawling features like the number of retweets, the number of followers, the subjectivity or objectivity of that tweet, the polarity of a tweet, and several other features. However, in this model, the likelihood of its virality is based upon the number of retweets.  The model developed showed promising results providing validation accuracy of 99.18%.

ANN model is used in this project. Model consists of 4 hidden layers.

Training 

Number of epochs = 100
Batch Size = 16
Training and Testing data split : 70% and 30% respectively.


Steps for running this project:

Step-1 : run dataset_generator.py

Step-2 : run model.py for training


Libraries used in this project :

1. Keras
2. Tweepy
3. Numpy
4. Pandas
5. Tensorflow
6. nltk for Natural Language Processing


