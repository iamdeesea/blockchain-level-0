import hashlib
import json
from typing import Any, Union


def calculate_hash(data: Union[str, dict, list], encoding: str = 'utf-8') -> str:
    """
    Calculate SHA-256 hash of input data.
    
    Args:
        data: The data to hash (string, dict, or list)
        encoding: Character encoding for string conversion
    
    Returns:
        Hexadecimal SHA-256 hash string
    """
    if isinstance(data, dict) or isinstance(data, list):
        data = json.dumps(data, sort_keys=True)
    
    if isinstance(data, str):
        data = data.encode(encoding)
    
    return hashlib.sha256(data).hexdigest()


def verify_hash(data: Union[str, dict, list], hash_value: str, encoding: str = 'utf-8') -> bool:
    """
    Verify if calculated hash matches the given hash.
    
    Args:
        data: The data to verify
        hash_value: The hash to compare against
        encoding: Character encoding for string conversion
    
    Returns:
        True if hashes match, False otherwise
    """
    calculated = calculate_hash(data, encoding)
    return calculated == hash_value


def double_hash(data: Union[str, dict, list], encoding: str = 'utf-8') -> str:
    """
    Apply SHA-256 twice (used in blockchain for extra security).
    
    Args:
        data: The data to hash
        encoding: Character encoding for string conversion
    
    Returns:
        Hexadecimal double SHA-256 hash string
    """
    first_hash = calculate_hash(data, encoding)
    return calculate_hash(first_hash, encoding)
