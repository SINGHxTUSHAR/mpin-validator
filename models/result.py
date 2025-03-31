## This file contains the ValidationResult class
class ValidationResult:
    def __init__(self, strength, reasons=None):
        """
        Initialize the validation result
        
        Args:
            strength (str): STRONG or WEAK
            reasons (list): List of reasons why the MPIN is considered weak
        """
        self.strength = strength
        self.reasons = reasons if reasons else []
    
    def __str__(self):
        if self.strength == "STRONG":
            return "Strength: STRONG"
        else:
            return f"Strength: WEAK\nReasons: {self.reasons}"