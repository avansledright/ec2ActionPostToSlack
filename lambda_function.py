import logging
import requests
import boto3
import os
from urllib.parse import unquote_plus
from slack import WebClient
from slack.errors import SlackApiError
logging.basicConfig(level=logging.DEBUG)

# Check EC2 Status
def lambda_handler(event, context):
    detail = event['detail']
    ids = detail['instance-id']
    eventname = detail['state']
    ec2 = boto3.resource('ec2')
# Slack Variables
    slack_token = os.environ["slackBot"]
    client = WebClient(token=slack_token)
    channel_string = "somestringhere"

# Post to slack that the instance is running
    if eventname == 'Running':
        try:
          instance = ec2.Instance(ids)
          response_string = f"The instance: {instance} has started"
          response = client.chat_postMessage(
            channel= channel_string,
          	text="An Instance has started",
           	blocks = [{"type": "section", "text": {"type": "plain_text", "text": response_string}}]
	        	)
        except SlackApiError as e:
          assert e.response["error"]  

		#Post to slack that instance is shutting down
    elif eventname == 'shutting-down':
    	try:
	        instance = ec2.Instance(ids)
	        response_string = f"The instance: {instance} is shutting down"
	        response = client.chat_postMessage(
	        	channel= channel_string,
	        	text="An Instance has started",
	        	blocks = [{"type": "section", "text": {"type": "plain_text", "text": response_string}}]
	        	)
    	except SlackApiError as e:
           assert e.response["error"]
	      	
    elif eventname == 'stopped':
    	try:
	        instance = ec2.Instance(ids)
	        response_string = f"The instance: {instance} has stopped"
	        response = client.chat_postMessage(
	        	channel= channel_string,
	        	text="An Instance has started",
	        	blocks = [{"type": "section", "text": {"type": "plain_text", "text": response_string}}]
	        	)
    	except SlackApiError as e:
    		assert e.response["error"]
	      	
    elif eventname == 'stopping':
    	try:
	        instance = ec2.Instance(ids)
	        response_string = f"The instance: {instance} is stopping"
	        response = client.chat_postMessage(
	        	channel= channel_string,
	        	text="An Instance has started",
	        	blocks = [{"type": "section", "text": {"type": "plain_text", "text": response_string}}]
	        	)
    	except SlackApiError as e:
    		assert e.response["error"]