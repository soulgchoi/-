from hashlib import sha256

class Block:
    def __init__(self, data, previous_hash, nonce=0):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self):
        print('nonce: ', self.nonce)
        print('data: ', self.data)
        print('previous hash: ', self.previous_hash)
        print('current hash: ', self.generate_hash())
        print()
    
    def generate_hash(self):
        block_contents = str(self.data) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_data = []
        self.genesis_block()

    def genesis_block(self):
        data = 'Genesis Block'
        block = Block(data, 0)
        self.chain.append(block)
        Block.print_block(block)
        return self.chain

    def add_block(self, data):
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(data, previous_block_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        Block.print_block(new_block)
        return proof, new_block

    def proof_of_work(self, block, difficulty=5):
        proof = block.generate_hash()

        while proof[:5] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        return proof


ssafy = Blockchain()
ssafy.add_block('2nd')
ssafy.add_block('3rd')