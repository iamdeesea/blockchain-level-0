"""Basic Blockchain Example - Create a simple chain"""
import sys
sys.path.insert(0, '..')

from blockchain import Blockchain
from transaction import Transaction

def main():
    # Create a new blockchain
    print("Creating blockchain...")
    blockchain = Blockchain(difficulty=2)
    print(f"Genesis block created: {blockchain.chain[0].hash}\n")
    
    # Create some transactions
    print("Creating transactions...")
    tx1 = Transaction('Alice', 'Bob', 50)
    tx2 = Transaction('Bob', 'Charlie', 25)
    tx3 = Transaction('Charlie', 'Alice', 10)
    
    print(f"  {tx1}")
    print(f"  {tx2}")
    print(f"  {tx3}")
    print()
    
    # Add transactions to blockchain
    print("Adding first block...")
    block1 = blockchain.add_block([tx1, tx2])
    print(f"Block 1 mined: {block1.hash}")
    print(f"  Nonce: {block1.nonce}")
    print(f"  Transactions: {len(block1.transactions)}\n")
    
    print("Adding second block...")
    block2 = blockchain.add_block([tx3])
    print(f"Block 2 mined: {block2.hash}")
    print(f"  Nonce: {block2.nonce}")
    print(f"  Transactions: {len(block2.transactions)}\n")
    
    # Verify chain
    print("Verifying blockchain...")
    is_valid = blockchain.is_chain_valid()
    print(f"Blockchain valid: {is_valid}\n")
    
    # Get chain info
    print("Chain Summary:")
    print(f"  Total blocks: {blockchain.get_chain_length()}")
    print(f"  Total transactions: {len(blockchain.get_all_transactions())}")
    print(f"  Latest block hash: {blockchain.get_latest_block().hash}")

if __name__ == '__main__':
    main()
