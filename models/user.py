class User:
    def __init__(self, dob=None, spouse_dob=None, anniversary=None):
        """
        Initialize the User with demographic information
        
        Args:
            dob (str): Date of birth in DD-MM-YYYY format
            spouse_dob (str): Spouse's date of birth in DD-MM-YYYY format
            anniversary (str): Wedding anniversary in DD-MM-YYYY format
        """
        from common.utils import parse_date
        
        self.dob = parse_date(dob)
        self.spouse_dob = parse_date(spouse_dob)
        self.anniversary = parse_date(anniversary)