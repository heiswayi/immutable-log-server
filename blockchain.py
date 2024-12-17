import json
import hashlib
import os
import time


class Blockchain:
    def __init__(self, filename="blockchain.json"):
        os.makedirs("data", exist_ok=True)
        self.filename = f"data/{filename}"
        self.chain = []
        self.load_chain()

    def create_genesis_block(self):
        """Create the first block of the blockchain."""
        genesis_block = {
            "index": 0,
            "timestamp": time.time(),
            "data": "Genesis Block",
            "previous_hash": "0",
            "hash": self.calculate_hash(0, time.time(), "Genesis Block", "0"),
        }
        self.chain.append(genesis_block)
        self.save_chain()

    def calculate_hash(self, index, timestamp, data, previous_hash):
        """Calculate SHA-256 hash of the block."""
        block_string = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data):
        """Add a new block to the blockchain."""
        previous_block = self.chain[-1]
        index = previous_block["index"] + 1
        timestamp = time.time()
        previous_hash = previous_block["hash"]
        new_hash = self.calculate_hash(index, timestamp, data, previous_hash)

        new_block = {
            "index": index,
            "timestamp": timestamp,
            "data": data,
            "previous_hash": previous_hash,
            "hash": new_hash,
        }
        self.chain.append(new_block)
        self.save_chain()
        return new_block

    def save_chain(self):
        """Save the blockchain to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.chain, file, indent=4)

    def load_chain(self):
        """Load the blockchain from a file."""
        try:
            with open(self.filename, "r") as file:
                self.chain = json.load(file)
        except FileNotFoundError:
            self.create_genesis_block()

    def validate_chain(self):
        """Check the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Validate hash
            if current["hash"] != self.calculate_hash(
                current["index"],
                current["timestamp"],
                current["data"],
                current["previous_hash"],
            ):
                return False

            # Validate previous hash
            if current["previous_hash"] != previous["hash"]:
                return False
        return True

    def get_logs(self):
        """Get all blocks (logs)."""
        return self.chain
