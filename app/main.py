from imap_connector import IMAPConnector

if __name__ == '__main__':
    conn = IMAPConnector()
    conn.get_mail_boxes()
    conn.logout()
