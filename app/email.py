import imaplib
import email
import os

from configparser import ConfigParser
from imaplib import IMAP4

CONFIG_FILE = "../config.cfg"

class IMAPConnector(object):

    def __init__(self):
        self.connection = self.get_connection()

    def get_connection(self):
        config = ConfigParser()
        config.read([CONFIG_FILE])

        hostname = config.get('server', 'hostname')
        connection = imaplib.IMAP4_SSL(hostname)

        username = config.get('account', 'username')
        password = config.get('account', 'password')
        connection.login(username, password)
        return connection

    def get_mail_list(self):
        return self.connection.list()

