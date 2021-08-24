"""

@Author: Rikesh Chhetri

@Date: 2021-08-18

@Last Modified by: Rikesh Chhetri

@Last Modified time: 2021-08-18 07:03:30

@Title : Program to perform live twitter sentiment analysis and visualization of those live data using socket.

"""
import socket
from  textblob import TextBlob
from loghandler import logger
import time
import csv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0',3337))
pos='positive'
neg='negative'
p_count=0
n_count=0

opinion = ["pos","neg","p_count","n_count"]
try:
   with open('data.csv', 'w') as csv_file:
         csv_writer = csv.DictWriter(csv_file, fieldnames=opinion)
         csv_writer.writeheader()

   while True:
   # printing line by line
      with open('data.csv', 'a') as csv_file:
            message = s.recv(1000)
            message = message.decode("utf-8")
            analysis=TextBlob(message) # here it will apply NLP\
            logger.info(analysis.sentiment)
            # now checking polarity only
            if analysis.sentiment.polarity > 0:
               logger.info("positive")
               p_count = p_count + 1
            elif analysis.sentiment[0]<0:
               logger.info("Negative")
               n_count = n_count + 1
            else :
               logger.info("Neutral")
            csv_writer = csv.DictWriter(csv_file, fieldnames=opinion)
            info = {
                     "pos": pos,
                     "neg": neg,
                     "p_count":p_count,
                     "n_count":n_count
                     }
            csv_writer.writerow(info)
            time.sleep(1) 
            print(p_count,n_count)
except Exception as e:
   logger.error(e)