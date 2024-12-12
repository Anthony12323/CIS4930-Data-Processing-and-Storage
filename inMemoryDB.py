class InMemoryDB:
    # initialize a public (accessible with "get") database 
    # and a mid-transaction placeholder "transaction_data"
    def __init__(self):
        self.database = {}
        self.transaction_data = None

    # returns the key found in the database, null (aka None) if not found
    def get(self, key):
        return self.database.get(key)

    # creates a new key (or assigns an existing key a new value) 
    # assuming a transaction is in progress
    def put(self, key, value):
        if self.transaction_data == None:
            raise Exception("No transaction currently in progress.")
        self.transaction_data[key] = value

    # begins a new transaction, throws an error if one is already in progress
    def begin_transaction(self):
        if self.transaction_data != None:
            raise Exception("A transaction is already in progress.")
        self.transaction_data = {}

    # commits any changes made to transaction_data to database, making it visible to "get" calls.
    # Also resets transaction_data, throws error if no transaction is taking place.
    def commit(self):
        if self.transaction_data == None:
            raise Exception("No transaction currently in progress.")
        self.database.update(self.transaction_data)
        self.transaction_data = None

    # Simply resets transaction_data so all changes made are not saved.
    # throws error if no transaction is taking place.
    def rollback(self):
        if self.transaction_data == None:
            raise Exception("No transaction currently in progress.")
        self.transaction_data = None

if __name__ == "__main__":
    # example usage:

    """
    inmemoryDB = InMemoryDB()

    inmemoryDB.get("A")
    
    inmemoryDB.put("A", 5)

    inmemoryDB.begin_transaction()

    inmemoryDB.put("A", 5)

    inmemoryDB.get("A")

    inmemoryDB.put("A", 6)

    inmemoryDB.commit()

    inmemoryDB.get("A")

    inmemoryDB.commit()

    inmemoryDB.rollback()

    inmemoryDB.get("B")

    inmemoryDB.begin_transaction()

    inmemoryDB.put("B", 10)

    inmemoryDB.rollback()

    inmemoryDB.get("B")
    """