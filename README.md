# EC2 Action Notification to Slack Channel
This Lambda function will notify a Slack channel of your choosing when an EC2 Action is performed.

## Usage
Notifications will trigger on the following EC2 Status
- starting
- stopping
- stopped
- shutting-down

You will need to configure a Slackbot with OAuth in order to utilize this function. The OAuth key will need to be set to an environment variable of $slackBot

### More Info
Read more about this function [here](https://aaron.vansledright.com/ec2-action-slack-notification/)