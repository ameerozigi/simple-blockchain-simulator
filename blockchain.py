import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            data=data,
            timestamp=time.time()
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash detected!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash detected!")
                return False

        return True

# Example usage
if __name__ == "__main__":
    my_blockchain = Blockchain()

    my_blockchain.add_block("First Block")
    my_blockchain.add_block("Second Block")
    my_blockchain.add_block("Third Block")

    for block in my_blockchain.chain:
        print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}]")

    print("Is blockchain valid?", my_blockchain.is_chain_valid())
