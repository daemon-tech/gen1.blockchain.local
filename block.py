import datetime

from hashlib import sha256

class Block:
  
  def __init__(self, transactions, previous_hash):
    self.time_stamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = 0
    self.hash = self.generate_hash()

  def generate_hash(self):
    block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
    block_hash = sha256(block_header.encode())
    block_hash_hex = block_hash.hexdigest()
    return block_hash_hex

  def print_contents(self):
    print("Data :")
    print("Timestamp -> ", self.time_stamp)
    print("Transactions -> ", self.transactions)
    print("Current Hash -> ", self.generate_hash())
    print("Previous Hash -> ", self.previous_hash) 
