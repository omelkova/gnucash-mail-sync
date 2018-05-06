import imaplib
import email
import logging
import os

from configparser import ConfigParser
from imaplib import IMAP4

logger = logging.getLogger("imap_connector")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

CONFIG_FILE = "config.cfg"

class IMAPConnector(object):

    def __init__(self):
        self.connection = self.get_connection()

    def get_connection(self):
        config = ConfigParser()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        logger.debug(dir_path)
        config.read([os.path.join(dir_path, CONFIG_FILE)])

        hostname = config.get('server', 'hostname')
        connection = imaplib.IMAP4_SSL(hostname)
        logger.info("Connecting to %s", hostname)

        username = config.get('account', 'username')
        password = config.get('account', 'password')
        connection.login(username, password)
        logger.info("Logging in as %s", username)
        return connection

    def logout(self):
        self.connection.logout()

    def get_mail_boxes(self):
        logger.info("Getting mail boxes")
        code, boxes = self.connection.list()
        logger.info("Response code: %s", code)
        if code is not "OK":
            return None
        return boxes



