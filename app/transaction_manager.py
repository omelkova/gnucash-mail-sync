import sys
from piecash import GnucashException, open_book, Split, Transaction

class TransactionManager(object):
    def __init__(self, gnucash_file, rules=None):
        self.rules = rules
        try:
            self.book = open_book(gnucash_file)
        except GnucashException as ex:
            print(ex)
            sys.exit()

    @property
    def accounts(self):
        return self.book.accounts

    def get_account(self, name):
        return self.book.accounts(name=name)

    def make_transaction(self, acc1, acc2, amount, description=None):
        if not description:
            description=""
        curr = self.book.default_currency
        splits = [
            Split(account=acc1, value=-amount),
            Split(account=acc2, value=amount)
        ]
        tr = Transaction(
            curr,
            description=description,
            splits=splits
        )
        # self.book.flush()
        self.book.save()

