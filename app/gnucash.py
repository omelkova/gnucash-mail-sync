from transaction_manager import TransactionManager
import piecash

GNUCASH_FILE = "example_file.gnucash"

# book = piecash.open_book(GNUCASH_FILE, readonly=True)
# print(book.default_currency)

book = TransactionManager(GNUCASH_FILE)

a1 = book.get_account("Assets")

a2 = book.get_account("Expence")

book.make_transaction(a1, a2, 20, description="Test transaction")

print(a1)
