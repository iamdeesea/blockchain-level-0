from typing import List, Optional
from hash_utils import calculate_hash
from transaction import Transaction


class MerkleTree:
    """
    Merkle Tree implementation for efficient transaction verification.
    
    A Merkle Tree is a binary tree where each leaf is a transaction hash
    and each parent is the hash of its children. The root hash can verify
    the entire set of transactions efficiently.
    """
    
    def __init__(self, transactions: List[Transaction]):
        """
        Build a Merkle Tree from transactions.
        
        Args:
            transactions: List of transactions to include in tree
        """
        self.transactions = transactions
        self.tree = []
        self.root = self._build_tree()
    
    def _build_tree(self) -> str:
        """
        Build the Merkle Tree from transactions.
        
        Returns:
            The root hash of the Merkle Tree
        """
        if not self.transactions:
            return '0' * 64  # Empty tree root
        
        # Create leaf hashes from transactions
        leaves = [calculate_hash(tx.to_dict()) for tx in self.transactions]
        self.tree.append(leaves)
        
        # Build tree level by level
        current_level = leaves
        while len(current_level) > 1:
            next_level = []
            
            # Pair up hashes and compute parent hash
            for i in range(0, len(current_level), 2):
                if i + 1 < len(current_level):
                    # Hash of two children
                    parent = calculate_hash(current_level[i] + current_level[i + 1])
                else:
                    # Odd number of nodes, duplicate last hash
                    parent = calculate_hash(current_level[i] + current_level[i])
                next_level.append(parent)
            
            self.tree.append(next_level)
            current_level = next_level
        
        return current_level[0]
    
    def get_proof(self, tx_index: int) -> List[tuple]:
        """
        Get the Merkle proof for a specific transaction.
        
        Args:
            tx_index: Index of transaction to get proof for
        
        Returns:
            List of (hash, position) tuples needed to verify the transaction
        """
        if tx_index >= len(self.transactions):
            return []
        
        proof = []
        index = tx_index
        
        # Traverse from leaf to root
        for level in self.tree[:-1]:
            if index % 2 == 0:
                # Current node is left child
                if index + 1 < len(level):
                    proof.append((level[index + 1], 'right'))
            else:
                # Current node is right child
                proof.append((level[index - 1], 'left'))
            
            index = index // 2
        
        return proof
    
    def verify_transaction(self, tx_index: int, proof: List[tuple]) -> bool:
        """
        Verify that a transaction is included in the tree.
        
        Args:
            tx_index: Index of transaction to verify
            proof: Merkle proof for the transaction
        
        Returns:
            True if transaction is verified, False otherwise
        """
        if tx_index >= len(self.transactions):
            return False
        
        # Calculate leaf hash
        tx = self.transactions[tx_index]
        current_hash = calculate_hash(tx.to_dict())
        
        # Traverse proof and recalculate root
        for proof_hash, position in proof:
            if position == 'left':
                current_hash = calculate_hash(proof_hash + current_hash)
            else:  # position == 'right'
                current_hash = calculate_hash(current_hash + proof_hash)
        
        # Verify root matches
        return current_hash == self.root
    
    def get_tree_structure(self) -> str:
        """
        Get a string representation of the tree structure.
        
        Returns:
            String showing all levels of the tree
        """
        result = "Merkle Tree Structure:\n"
        for level_idx, level in enumerate(self.tree):
            result += f"Level {level_idx}: "
            for hash_val in level:
                result += f"{hash_val[:8]}... "
            result += "\n"
        return result
