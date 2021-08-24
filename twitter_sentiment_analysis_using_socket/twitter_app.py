"""

@Author: Rikesh Chhetri

@Date: 2021-08-18

@Last Modified by: Rikesh Chhetri

@Last Modified time: 2021-08-18 07:03:30

@Title : Program to perform live twitter sentiment analysis and visualization of those live data using sockets.

"""
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import os
from dotenv import load_dotenv
load_dotenv('.env')



# Set up your credentials
# all 4 authentication keys to access twitter API
# to connect as OAth handler or jump server / revers proxy server
consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token =os.getenv("ACCESS_TOKEN")
access_secret=os.getenv("ACCESS_SECRET")


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['#Afghanistan'])

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "0.0.0.0"     # Get local machine name
  port = 3337                # Reserve a port for your service.

  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(4)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )