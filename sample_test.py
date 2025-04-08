#!/bin/env python3

# This sample demonstrates how to make and process the results of a subscription.

from activfinancial import *
from activfinancial.constants import *
from activfinancial.samples import common
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# This SubscriptionHandler class provides us with an interface for processing
# the results of our subscription.
class SubscriptionHandler:
	def on_subscription_refresh(self, msg, context):
		print(f'REFRESH received for {msg.symbol}')
		print(common.refresh_message_to_string(msg, context.session.metadata))

	def on_subscription_update(self, msg, context):
		print(f'UPDATE received for {msg.symbol}')
		print(common.update_message_to_string(msg, context.session.metadata))

	def on_subscription_topic_status(self, msg, context):
		print(f'TOPIC STATUS received for {msg.symbol}')
		print(common.topic_status_message_to_string(msg))

	def on_subscription_status(self, msg, context):
		print(f'SUBSCRIPTION STATUS received for {msg.request}')
		print(common.subscription_status_message_to_string(msg))

# Create the session.
# Enable a CTRL handler to exit cleanly on CTRL-C/CTRL-BREAK.
session = Session({ FID_ENABLE_CTRL_HANDLER: True },
				  handler=common.PrintSessionHandler())

# Get connection parameters from environment variables
# Use variable names found in .env file
connect_parameters = {
    FID_HOST: os.getenv('ACTIV_SESSION_HOST', 'aop-replay.activfinancial.com'),
    FID_USER_ID: os.getenv('ACTIV_SESSION_USER_ID', ''),
    FID_PASSWORD: os.getenv('ACTIV_SESSION_PASSWORD', '')
}

# Connect synchronously.
session.connect(connect_parameters)

# Request subscription of the Canadian Solar Inc US Equity topic.
session.subscribe("CSIQ.Q", handler=SubscriptionHandler())

# Run the internal session message loop.
session.run()
