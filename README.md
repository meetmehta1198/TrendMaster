# Virality Predictor
The project consists of a model that can predict whether a given tweet will be viral or not. For model training, the dataset is prepared by web scrapping using tweepy API in python.  In addition to that, through web crawling features like the number of retweets, the number of followers, the subjectivity or objectivity of that tweet, the polarity of a tweet, and several other features. However, in this model, the likelihood of its virality is based upon the number of retweets.  The model developed showed promising results providing validation accuracy of 99.18%.

ANN model is used in this project. Model consists of 4 hidden layers.

Training 

Number of epochs = 100
Batch Size = 16
Training and Testing data split : 70% and 30% respectively.


Steps for running this project:

Step-1 : Create your account in twitter-developer and register your application in order to get access to twitter for scraping.

Step-2 : run dataset_generator.py with proper access key and consumer key tokens.

Step-3 : run model.py for training


Steps for creating account in twitter-developer and registering your application:

Follow article on this link : https://medium.com/@divyeshardeshana/create-twitter-developer-account-app-4ac55e945bf4


Libraries used in this project :

1. Keras
2. Tweepy
3. Numpy
4. Pandas
5. Tensorflow
6. nltk for Natural Language Processing


