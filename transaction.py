from datetime import datetime
from typing import Optional, Dict, Any
import json


class Transaction:
    """
    Represents a transaction in the blockchain.
    
    Attributes:
        sender (str): Address or ID of the sender
        receiver (str): Address or ID of the receiver
        amount (float): Amount being transferred
        timestamp (str): When the transaction occurred
        transaction_id (Optional[str]): Unique identifier for the transaction
    """
    
    def __init__(
        self,
        sender: str,
        receiver: str,
        amount: float,
        timestamp: Optional[str] = None,
        transaction_id: Optional[str] = None
    ):
        """
        Initialize a transaction.
        
        Args:
            sender: Who is sending
            receiver: Who is receiving
            amount: How much is being sent
            timestamp: When the transaction happened (defaults to now)
            transaction_id: Optional ID (can be auto-generated)
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = timestamp or datetime.now().isoformat()
        self.transaction_id = transaction_id
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert transaction to dictionary for hashing.
        
        Returns:
            Dictionary representation of the transaction
        """
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp
        }
    
    def to_json(self) -> str:
        """
        Convert transaction to JSON string.
        
        Returns:
            JSON string representation
        """
        return json.dumps(self.to_dict(), sort_keys=True)
    
    def is_valid(self) -> bool:
        """
        Validate transaction data.
        
        Returns:
            True if transaction is valid, False otherwise
        """
        # Check if sender and receiver exist
        if not self.sender or not self.receiver:
            return False
        
        # Check if amount is positive
        if self.amount <= 0:
            return False
        
        # Check if sender and receiver are different
        if self.sender == self.receiver:
            return False
        
        return True
    
    def __repr__(self) -> str:
        """
        String representation of transaction.
        """
        return (f"Transaction({self.sender} -> {self.receiver}: "
                f"{self.amount} @ {self.timestamp})")
    
    def __str__(self) -> str:
        """
        Human-readable string representation.
        """
        return (f"{self.sender} sends {self.amount} to {self.receiver}"
                f" on {self.timestamp}")
