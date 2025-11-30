from typing import List
from block import Block
from transaction import Transaction


class Blockchain:
    """
    Represents the blockchain - a chain of validated blocks.
    
    Attributes:
        chain (List[Block]): List of blocks in the blockchain
        pending_transactions (List[Transaction]): Transactions waiting to be added
        difficulty (int): Mining difficulty for new blocks
    """
    
    def __init__(self, difficulty: int = 2):
        """
        Initialize blockchain with genesis block.
        
        Args:
            difficulty: Number of leading zeros required in block hash
        """
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = difficulty
        
        # Create genesis block
        genesis_block = Block(
            index=0,
            transactions=[],
            previous_hash='0',
            difficulty=self.difficulty
        )
        genesis_block.mine_block()
        self.chain.append(genesis_block)
    
    def add_transaction(self, transaction: Transaction) -> bool:
        """
        Add a transaction to pending transactions.
        
        Args:
            transaction: Transaction to add
        
        Returns:
            True if added successfully, False if invalid
        """
        if not transaction.is_valid():
            return False
        
        self.pending_transactions.append(transaction)
        return True
    
    def add_block(self, transactions: List[Transaction] = None) -> Block:
        """
        Create and add a new block to the blockchain.
        
        Args:
            transactions: List of transactions for the block. If None, uses pending.
        
        Returns:
            The newly created and mined block
        """
        if transactions is None:
            transactions = self.pending_transactions
            self.pending_transactions = []
        
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=self.chain[-1].hash,
            difficulty=self.difficulty
        )
        
        new_block.mine_block()
        self.chain.append(new_block)
        return new_block
    
    def get_latest_block(self) -> Block:
        """
        Get the last block in the chain.
        
        Returns:
            The most recent block
        """
        return self.chain[-1]
    
    def is_chain_valid(self) -> bool:
        """
        Verify the entire blockchain integrity.
        
        Returns:
            True if chain is valid, False if tampering detected
        """
        # Check each block except genesis
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Verify current block references previous block correctly
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify Proof of Work
            if not current_block.is_valid_proof_of_work():
                return False
        
        return True
    
    def get_chain_length(self) -> int:
        """
        Get the number of blocks in the chain.
        
        Returns:
            Length of blockchain
        """
        return len(self.chain)
    
    def get_all_transactions(self) -> List[Transaction]:
        """
        Get all transactions from all blocks in the chain.
        
        Returns:
            List of all transactions
        """
        all_transactions = []
        for block in self.chain:
            all_transactions.extend(block.transactions)
        return all_transactions
