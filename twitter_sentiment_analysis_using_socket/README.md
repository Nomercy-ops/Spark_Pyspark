# Live twitter sentiments analysis and visualization of counts of positive and negative tweets using socket

## Note:
* Sentiment analysis on streaming twitter data using Tweepy Textblob python
* This project is a good starting point for those who have little or no experience with  We use Twitter data since Twitter provides an API for developers that is easy to access.
* We present how to stream data from Twitter and  apply a simple sentiment analysis model to detect the polarity and subjectivity of each tweet.

## We will  use Python Notebook 

## Main Libraries
* Tweepy:  interact with the Twitter Streaming API and create a live data streaming pipeline with Twitter
* create socket to recieve twitter data on client side.
* Textblob:  apply sentiment analysis on the twitter text data 


## Part 1: Send tweets from the Twitter API 
* In this part, we use our developer credentials to authenticate and connect to the Twitter API. Here, we use Python's Tweepy library for connecting and getting the tweets from the Twitter API. 

* Code:

## check twitter_analysis.ipynb file

## create a socket to recieve stream data from tweepy tcp port: 0.0.0.0:5557

## Part 2: Tweet preprocessing and sentiment analysis
* In this part, we receive the data Then, we apply sentiment analysis using textblob, which is Python's library for processing textual * data. After sentiment analysis, we save the tweet and the sentiment analysis scores and apply logic to get positive and negative counts and then save those data live in a csv file.

* Code:

## check twitter_analysis.ipynb file

## Part 3: live bar plot visualization of tweets:
* Here we will open another file plotdata.ipynb and run it for the live visualization of positive and negative tweets in a bar graph using matplotlib library.

### check the video link:


