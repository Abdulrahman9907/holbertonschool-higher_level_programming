#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.
    
    Args:
        c: A character to check
        
    Returns:
        True if c is lowercase, False otherwise
    """
    # Get ASCII value of the character
    ascii_val = ord(c)
    
    # Lowercase letters 'a' to 'z' have ASCII values 97 to 122
    if ascii_val >= 97 and ascii_val <= 122:
        return True
    else:
        return False
