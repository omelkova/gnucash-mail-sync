import piecash

GNUCASH_FILE = "example_file.gnucash"

book = piecash.open_book(GNUCASH_FILE, readonly=True)

for account in book.accounts:
    print(account)
