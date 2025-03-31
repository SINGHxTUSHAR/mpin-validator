from models.user import User
from models.result import ValidationResult
from validators.common_mpin import CommonMPINValidator
from validators.demographic import DemographicValidator
from common.constants import Constants

class MPINValidator:
    @staticmethod
    def validate_mpin_part_a(mpin):
        """
        Part A: Check if the 4-digit MPIN is commonly used
        
        Args:
            mpin (str): 4-digit MPIN
        
        Returns:
            bool: True if commonly used, False otherwise
        """
        if len(mpin) != 4 or not mpin.isdigit():
            raise ValueError("MPIN must be a 4-digit number")

        return CommonMPINValidator.is_weak_common_mpin(mpin)

    @staticmethod
    def validate_mpin_part_b(mpin, dob=None, spouse_dob=None, anniversary=None):
        """
        Part B: Check if the MPIN is strong or weak based on common patterns and demographics
        
        Args:
            mpin (str): 4-digit MPIN
            dob (str): Date of birth in DD-MM-YYYY format
            spouse_dob (str): Spouse's date of birth in DD-MM-YYYY format
            anniversary (str): Wedding anniversary in DD-MM-YYYY format
        
        Returns:
            str: STRONG or WEAK
        """
        if len(mpin) != 4 or not mpin.isdigit():
            raise ValueError("MPIN must be a 4-digit number")

        # Check common patterns
        if CommonMPINValidator.is_weak_common_mpin(mpin):
            return Constants.WEAK
        
        # Check demographic patterns
        user = User(dob, spouse_dob, anniversary)
        demographic_reasons = DemographicValidator.check_demographic_match(mpin, user)
        
        if demographic_reasons:
            return Constants.WEAK
        
        return Constants.STRONG

    @staticmethod
    def validate_mpin_part_c(mpin, dob=None, spouse_dob=None, anniversary=None):
        """
        Part C: Check if the MPIN is strong or weak and provide reasons if weak
        
        Args:
            mpin (str): 4-digit MPIN
            dob (str): Date of birth in DD-MM-YYYY format
            spouse_dob (str): Spouse's date of birth in DD-MM-YYYY format
            anniversary (str): Wedding anniversary in DD-MM-YYYY format
        
        Returns:
            ValidationResult: Result object with strength and reasons
        """
        if len(mpin) != 4 or not mpin.isdigit():
            raise ValueError("MPIN must be a 4-digit number")

        reasons = []
        
        # Check common patterns
        if CommonMPINValidator.is_weak_common_mpin(mpin):
            reasons.append(Constants.COMMONLY_USED)
        
        # Check demographic patterns
        user = User(dob, spouse_dob, anniversary)
        demographic_reasons = DemographicValidator.check_demographic_match(mpin, user)
        reasons.extend(demographic_reasons)
        
        if reasons:
            return ValidationResult(Constants.WEAK, reasons)
        
        return ValidationResult(Constants.STRONG)

    @staticmethod
    def validate_mpin_part_d(mpin, dob=None, spouse_dob=None, anniversary=None):
        """
        Part D: Check if the 6-digit MPIN is strong or weak and provide reasons if weak
        
        Args:
            mpin (str): 6-digit MPIN
            dob (str): Date of birth in DD-MM-YYYY format
            spouse_dob (str): Spouse's date of birth in DD-MM-YYYY format
            anniversary (str): Wedding anniversary in DD-MM-YYYY format
        
        Returns:
            ValidationResult: Result object with strength and reasons
        """
        if len(mpin) != 6 or not mpin.isdigit():
            raise ValueError("MPIN must be a 6-digit number")

        reasons = []
        
        # Check common patterns
        if CommonMPINValidator.is_weak_common_mpin(mpin):
            reasons.append(Constants.COMMONLY_USED)
        
        # Check demographic patterns
        user = User(dob, spouse_dob, anniversary)
        demographic_reasons = DemographicValidator.check_demographic_match(mpin, user)
        reasons.extend(demographic_reasons)
        
        if reasons:
            return ValidationResult(Constants.WEAK, reasons)
        
        return ValidationResult(Constants.STRONG)