## This file contains the DemographicValidator class
from common.constants import Constants
from common.utils import generate_date_variants

class DemographicValidator:
    @staticmethod
    def check_demographic_match(mpin, user):
        """
        Check if the MPIN matches any demographic information
        
        Args:
            mpin (str): The MPIN to validate
            user (User): User object with demographic information
        
        Returns:
            list: List of demographic match reasons, empty if no match found
        """
        reasons = []
        
        # Check DOB of self
        if user.dob:
            dob_variants = generate_date_variants(user.dob)
            if any(variant == mpin for variant in dob_variants):
                reasons.append(Constants.DEMOGRAPHIC_DOB_SELF)
        
        # Check spouse's DOB
        if user.spouse_dob:
            spouse_dob_variants = generate_date_variants(user.spouse_dob)
            if any(variant == mpin for variant in spouse_dob_variants):
                reasons.append(Constants.DEMOGRAPHIC_DOB_SPOUSE)
        
        # Check anniversary
        if user.anniversary:
            anniversary_variants = generate_date_variants(user.anniversary)
            if any(variant == mpin for variant in anniversary_variants):
                reasons.append(Constants.DEMOGRAPHIC_ANNIVERSARY)
        
        return reasons