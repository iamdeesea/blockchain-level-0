# Blockchain Level 0

A foundational blockchain learning repository covering Level 0 concepts: blocks, hashing, transactions, and chain validation. Includes practical implementations in Python.

## 📚 Table of Contents

- [Overview](#overview)
- [Key Concepts](#key-concepts)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Core Components](#core-components)
- [Usage Examples](#usage-examples)
- [Learning Path](#learning-path)

## Overview

This repository provides a hands-on introduction to blockchain fundamentals without the complexity of consensus mechanisms or cryptographic signatures. It focuses on:

- **Block structure** and data organization
- **Hashing** and data integrity
- **Transaction representation** and validation
- **Chain linking** and integrity verification
- **Merkle trees** for efficient data verification

## Key Concepts

### 1. Blocks
A block is a container for transactions with metadata:
```
Block {
  index: int,
  timestamp: str,
  transactions: list,
  previous_hash: str,
  hash: str,
  nonce: int
}
```

### 2. Hashing
Using SHA-256 to create immutable fingerprints of block data:
- Deterministic (same input = same output)
- One-way (cannot reverse)
- Avalanche effect (small change = completely different hash)

### 3. Transactions
Representing value transfers:
```
Transaction {
  sender: str,
  receiver: str,
  amount: float,
  timestamp: str
}
```

### 4. Chain Validation
Ensuring chain integrity by verifying:
- Each block's hash matches its calculated value
- Each block references the previous block's hash
- Transactions are well-formed

## Project Structure

```
blockchain-level-0/
├── block.py              # Block class implementation
├── blockchain.py         # Blockchain class implementation
├── transaction.py        # Transaction class implementation
├── merkle_tree.py        # Merkle tree implementation
├── hash_utils.py         # Hashing utilities
├── examples/
│   ├── basic_chain.py    # Simple blockchain example
│   ├── validation.py     # Chain validation example
│   └── transactions.py   # Transaction handling example
├── tests/
│   ├── test_block.py     # Block tests
│   ├── test_blockchain.py # Blockchain tests
│   └── test_transaction.py # Transaction tests
├── README.md
├── requirements.txt
└── LICENSE
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/iamdeesea/blockchain-level-0.git
cd blockchain-level-0

# Install dependencies
pip install -r requirements.txt
```

### Quick Start

```python
from blockchain import Blockchain
from transaction import Transaction

# Create blockchain
bc = Blockchain()

# Create transactions
tx1 = Transaction('Alice', 'Bob', 50)
tx2 = Transaction('Bob', 'Charlie', 25)

# Add block with transactions
bc.add_block([tx1, tx2])

# Verify chain
if bc.is_chain_valid():
    print("Blockchain is valid!")
```

## Core Components

### Block
- Stores block metadata and transactions
- Calculates and stores SHA-256 hash
- Implements Proof of Work (simple difficulty)

### Blockchain
- Manages chain of blocks
- Validates chain integrity
- Adds new blocks
- Provides chain information

### Transaction
- Represents value transfer
- Contains sender, receiver, amount, timestamp
- Can be validated for format

### Merkle Tree
- Efficiently represents transaction set
- Root hash for quick integrity checking
- Enables partial validation

## Usage Examples

### Example 1: Creating a Simple Chain

```python
from blockchain import Blockchain
from transaction import Transaction

bc = Blockchain()

# Add first block
block1 = bc.add_block([
    Transaction('Alice', 'Bob', 100),
    Transaction('Bob', 'Charlie', 50)
])

# Add second block
block2 = bc.add_block([
    Transaction('Charlie', 'Alice', 25)
])

print(f"Chain length: {len(bc.chain)}")
print(f"Last block hash: {bc.chain[-1].hash}")
```

### Example 2: Validating the Chain

```python
# Tamper with a transaction
bc.chain[0].transactions[0].amount = 999999

# Verify chain
if not bc.is_chain_valid():
    print("Tampered block detected!")
```

### Example 3: Merkle Tree Verification

```python
from merkle_tree import MerkleTree
from transaction import Transaction

transactions = [
    Transaction('Alice', 'Bob', 100),
    Transaction('Bob', 'Charlie', 50),
    Transaction('Charlie', 'Alice', 25)
]

merkle = MerkleTree(transactions)
print(f"Merkle Root: {merkle.root}")
```

## Learning Path

1. **Week 1**: Understand Block structure and hashing
   - Read: Block class and SHA-256 hashing
   - Exercise: Create and modify blocks, observe hash changes

2. **Week 2**: Transaction representation
   - Read: Transaction class implementation
   - Exercise: Create and validate transactions

3. **Week 3**: Building a blockchain
   - Read: Blockchain class and validation logic
   - Exercise: Build a simple chain and validate it

4. **Week 4**: Advanced concepts
   - Read: Merkle trees and chain analytics
   - Exercise: Implement merkle tree verification

## Next Steps

After mastering Level 0, explore:
- **Level 1**: Consensus mechanisms (Proof of Work, Proof of Stake)
- **Level 2**: Digital signatures and asymmetric cryptography
- **Level 3**: Smart contracts and state management
- **Level 4**: Distributed networks and P2P protocols

## Resources

- [Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)
- [Ethereum Docs](https://ethereum.org/)
- [Mastering Bitcoin](https://github.com/bitcoinbook/bitcoinbook)
- [Blockchain Basics Course](https://www.coursera.org/learn/blockchain-basics)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

MIT License - See LICENSE file for details

## Author

Built for learning blockchain fundamentals.
