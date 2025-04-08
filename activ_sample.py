#!/bin/env python3

# This sample demonstrates how to connect to a Gateway and subscribe to a symbol.

from activfinancial import *
from activfinancial.constants import *
import os
import logging
import sys
import time
from activfinancial import Session
from activfinancial.constants import (
    DATA_SOURCE_ACTIV, 
    SYMBOLOGY_NATIVE,
    FID_ENABLE_CTRL_HANDLER,
    FID_ENABLE_DICTIONARY_DOWNLOAD,
    FID_HOST,
    FID_USER_ID,
    FID_PASSWORD
)

# Configure basic logging
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for more detailed logging
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout  # Explicitly set output to stdout
)
logger = logging.getLogger(__name__)

# Get the DLL directory path
dll_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                      "venv", "Lib", "site-packages", "activfinancial", "lib")

# Add DLL directory to system path
if hasattr(os, 'add_dll_directory'):
    os.add_dll_directory(dll_dir)

# Add DLL directory to PATH environment variable
if 'PATH' in os.environ:
    os.environ['PATH'] = dll_dir + os.pathsep + os.environ['PATH']
else:
    os.environ['PATH'] = dll_dir

# Set ACTIV_ONE_API_PATH environment variable
os.environ['ACTIV_ONE_API_PATH'] = dll_dir

# This SubscriptionHandler class provides us with an interface for processing
# the results of our subscription.
class SubscriptionHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def on_refresh(self, msg, context):
        """Handle refresh messages."""
        try:
            self.logger.info(f"**** Refresh on subscription {context.handle} ****")
            self.logger.info(f"Data source ................................. {msg.data_source_id}")
            self.logger.info(f"Symbology ................................... {msg.symbology_id}")
            self.logger.info(f"Symbol ...................................... {msg.symbol}")
            self.logger.info(f"Topic subscription state .................... {msg.topic_subscription_state}")
            self.logger.info(f"Topic type .................................. {msg.topic_type}")
            self.logger.info(f"Update id ................................... {msg.update_id}")
            self.logger.info(f"Permission id ............................... {msg.permission_id}")
            
            # Log field values if available
            if hasattr(msg, 'fields'):
                for field_id, value in msg.fields.items():
                    self.logger.info(f"Field {field_id} ..................................... {value}")
        except Exception as e:
            self.logger.error(f"Error in on_refresh: {str(e)}", exc_info=True)

    def on_update(self, msg, context):
        """Handle update messages."""
        try:
            self.logger.info(f"**** Update on subscription {context.handle} ****")
            self.logger.info(f"Data source ................................. {msg.data_source_id}")
            self.logger.info(f"Symbology ................................... {msg.symbology_id}")
            self.logger.info(f"Symbol ...................................... {msg.symbol}")
            self.logger.info(f"Update type ................................. {msg.update_type}")
            self.logger.info(f"Topic subscription state .................... {msg.topic_subscription_state}")
            self.logger.info(f"Topic type .................................. {msg.topic_type}")
            self.logger.info(f"Update id ................................... {msg.update_id}")
            self.logger.info(f"Event type .................................. {msg.event_type}")
            self.logger.info(f"Permission id ............................... {msg.permission_id}")
            
            # Log field values if available
            if hasattr(msg, 'fields'):
                for field_id, value in msg.fields.items():
                    self.logger.info(f"Field {field_id} ..................................... {value}")
        except Exception as e:
            self.logger.error(f"Error in on_update: {str(e)}", exc_info=True)

    def on_subscription_status(self, msg, context):
        """Handle subscription status messages."""
        try:
            self.logger.info(f"**** Status on subscription {context.handle} ****")
            self.logger.info(f"Data source ................................. {msg.data_source_id}")
            self.logger.info(f"Symbology ................................... {msg.symbology_id}")
            self.logger.info(f"Request ..................................... {msg.request}")
            self.logger.info(f"State ....................................... {msg.state}")
        except Exception as e:
            self.logger.error(f"Error in on_subscription_status: {str(e)}", exc_info=True)

    def on_topic_status(self, msg, context):
        """Handle topic status messages."""
        try:
            self.logger.info(f"**** Topic status on subscription {context.handle} ****")
            self.logger.info(f"Data source ................................. {msg.data_source_id}")
            self.logger.info(f"Symbology ................................... {msg.symbology_id}")
            self.logger.info(f"Symbol ...................................... {msg.symbol}")
            self.logger.info(f"Topic subscription state .................... {msg.topic_subscription_state}")
            self.logger.info(f"Topic type .................................. {msg.topic_type}")
        except Exception as e:
            self.logger.error(f"Error in on_topic_status: {str(e)}", exc_info=True)

# This SessionHandler class provides us with an interface for processing
# session events.
class SessionHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def on_connected(self, session):
        """Handle connection events."""
        try:
            self.logger.info("Session connected")
        except Exception as e:
            self.logger.error(f"Error in on_connected: {str(e)}", exc_info=True)

    def on_disconnected(self, session):
        """Handle disconnection events."""
        try:
            self.logger.info("Session disconnected")
        except Exception as e:
            self.logger.error(f"Error in on_disconnected: {str(e)}", exc_info=True)

    def on_error(self, session, error):
        """Handle error events."""
        try:
            self.logger.error(f"Session error: {error}")
        except Exception as e:
            self.logger.error(f"Error in on_error: {str(e)}", exc_info=True)

    def on_log(self, session, log_type, message):
        """Handle log messages."""
        try:
            self.logger.info(f"Session log: {message}")
        except Exception as e:
            self.logger.error(f"Error in on_log: {str(e)}", exc_info=True)

def main():
    try:
        # Set environment variables
        host = 'aop-replay.activfinancial.com'
        user_id = 'fitesystem-replay'
        password = '85jf73l9'  # Updated password

        logger.info("Environment variables set:")
        logger.info(f"Host: {host}")
        logger.info(f"User ID: {user_id}")
        logger.info(f"ACTIV_ONE_API_PATH: {os.environ['ACTIV_ONE_API_PATH']}")
        logger.info(f"PATH: {os.environ['PATH']}")

        # Create handlers
        session_handler = SessionHandler()
        subscription_handler = SubscriptionHandler()

        # Create session parameters
        session_parameters = {
            FID_ENABLE_CTRL_HANDLER: True,
            FID_ENABLE_DICTIONARY_DOWNLOAD: True,
            FID_HOST: host,
            FID_USER_ID: user_id,
            FID_PASSWORD: password
        }

        # Create and connect session
        logger.info("Creating session...")
        session = Session(session_parameters, session_handler)
        
        logger.info("Connecting to %s as %s...", host, user_id)
        # Connect with a 5-second timeout
        session.connect(timeout=5000)

        # Subscribe to Microsoft stock
        logger.info("Subscribing to MSFT.Q...")
        session.subscribe("MSFT.Q", subscription_handler, 
                         symbology_id=SYMBOLOGY_NATIVE, 
                         data_source_id=DATA_SOURCE_ACTIV)

        # Run the internal session message loop
        logger.info("Starting message loop...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Shutting down...")
            session.disconnect()
    except Exception as e:
        logger.error(f"Error in main: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 