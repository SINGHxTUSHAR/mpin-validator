## This file contains the CommonMPINValidator class
from common.constants import Constants

class CommonMPINValidator:
    @staticmethod
    def is_common_mpin(mpin, length=4):
        """Check if the MPIN is in the list of commonly used MPINs"""
        if length == 4:
            return mpin in Constants.COMMON_MPINS_4
        else:  # length == 6
            return mpin in Constants.COMMON_MPINS_6
    
    @staticmethod
    def is_sequential(mpin):
        """Check if the MPIN has sequential digits (ascending or descending)"""
        # Check for ascending sequence
        has_ascending = False
        for i in range(len(mpin) - 3):
            if (int(mpin[i]) + 1 == int(mpin[i+1]) and 
                int(mpin[i+1]) + 1 == int(mpin[i+2]) and
                int(mpin[i+2]) + 1 == int(mpin[i+3])):
                has_ascending = True
                break
        
        # Check for descending sequence
        has_descending = False
        for i in range(len(mpin) - 3):
            if (int(mpin[i]) - 1 == int(mpin[i+1]) and 
                int(mpin[i+1]) - 1 == int(mpin[i+2]) and
                int(mpin[i+2]) - 1 == int(mpin[i+3])):
                has_descending = True
                break
        
        return has_ascending or has_descending
    
    @staticmethod
    def is_repeating(mpin):
        """Check if the MPIN has repeating digits"""
        for i in range(len(mpin) - 2):
            if mpin[i] == mpin[i+1] == mpin[i+2]:
                return True
        return False
    
    @staticmethod
    def has_pattern(mpin):
        """Check for common patterns in the MPIN"""
        # Check for repeating pairs (e.g., 1212, 2323)
        if len(mpin) >= 4 and mpin[0:2] == mpin[2:4]:
            return True
        
        # Check for palindrome
        if mpin == mpin[::-1] and len(mpin) > 2:
            return True
        
        return False
    
    @staticmethod
    def is_weak_common_mpin(mpin):
        """
        Check if the MPIN is weak based on common patterns
        
        Returns:
            bool: True if the MPIN is considered weak
        """
        length = len(mpin)
        
        # Check against common MPINs list
        if CommonMPINValidator.is_common_mpin(mpin, length):
            return True
        
        # Check for sequential digits
        if CommonMPINValidator.is_sequential(mpin):
            return True
        
        # Check for repeating digits
        if CommonMPINValidator.is_repeating(mpin):
            return True
        
        # Check for patterns
        if CommonMPINValidator.has_pattern(mpin):
            return True
        
        return False