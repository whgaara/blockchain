import hashlib
import json
from time import time


class BlockChain():
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        self.new_block(proof=100, previous_hash=1)


    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self):
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        '''
        simple proof for work
        function: find a 'p' for hash(pp') = '0000.....'
        :param
            p: proof for last block
            p': proof for current block
        '''
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = ('{' + last_proof + '}' + '{' + proof + '}').encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

    @staticmethod
    def hash(cls):
        '''
        product SHA-256 hash value
        '''
        block_string = json.dumps(cls, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]



