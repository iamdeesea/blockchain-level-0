from datetime import datetime
from typing import List, Optional, Dict, Any
import json
from hash_utils import calculate_hash
from transaction import Transaction


class Block:
    """
    Represents a block in the blockchain.
    
    Attributes:
        index (int): Position of block in the chain
        timestamp (str): When block was created
        transactions (List[Transaction]): List of transactions in block
        previous_hash (str): Hash of the previous block
        hash (str): Current block's hash
        nonce (int): Number used once for Proof of Work
        difficulty (int): Number of leading zeros required in hash
    """
    
    def __init__(
        self,
        index: int,
        transactions: List[Transaction],
        previous_hash: str = '0',
        difficulty: int = 2
    ):
        """
        Initialize a block.
        
        Args:
            index: Block's position in chain
            transactions: List of transactions
            previous_hash: Hash of previous block
            difficulty: Proof of Work difficulty (leading zeros)
        """
        self.index = index
        self.timestamp = datetime.now().isoformat()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculate SHA-256 hash of block data.
        
        Returns:
            Hexadecimal hash string
        """
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }
        return calculate_hash(block_data)
    
    def mine_block(self) -> None:
        """
        Mine the block using Proof of Work (simple difficulty).
        Incrementally adjusts nonce until hash meets difficulty requirement.
        """
        target = '0' * self.difficulty
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
    
    def is_valid_proof_of_work(self) -> bool:
        """
        Verify that block's hash meets Proof of Work requirements.
        
        Returns:
            True if hash has correct leading zeros, False otherwise
        """
        target = '0' * self.difficulty
        return self.hash[:self.difficulty] == target
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert block to dictionary.
        
        Returns:
            Dictionary representation of block
        """
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'hash': self.hash,
            'nonce': self.nonce,
            'difficulty': self.difficulty
        }
    
    def to_json(self) -> str:
        """
        Convert block to JSON string.
        
        Returns:
            JSON string representation
        """
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        """
        String representation of block.
        """
        return (f"Block(index={self.index}, tx_count={len(self.transactions)}, "
                f"hash={self.hash[:8]}..., nonce={self.nonce})")
    
    def __str__(self) -> str:
        """
        Human-readable string representation.
        """
        return (f"Block #{self.index}\n"
                f"Hash: {self.hash}\n"
                f"Previous: {self.previous_hash}\n"
                f"Transactions: {len(self.transactions)}\n"
                f"Nonce: {self.nonce}")
