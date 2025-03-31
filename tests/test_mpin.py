import unittest
from main import MPINValidator

class TestMPINValidator(unittest.TestCase):
    def test_part_a_common_mpins(self):
        """Test Part A with commonly used MPINs"""
        # Common MPINs should be identified as commonly used
        self.assertTrue(MPINValidator.validate_mpin_part_a("1234"))
        self.assertTrue(MPINValidator.validate_mpin_part_a("1111"))
        self.assertTrue(MPINValidator.validate_mpin_part_a("0000"))
        self.assertTrue(MPINValidator.validate_mpin_part_a("1122"))
        self.assertTrue(MPINValidator.validate_mpin_part_a("4321"))
        
    def test_part_a_strong_mpins(self):
        """Test Part A with strong MPINs"""
        # Less common MPINs should not be identified as commonly used
        self.assertFalse(MPINValidator.validate_mpin_part_a("7294"))
        self.assertFalse(MPINValidator.validate_mpin_part_a("8156"))
        self.assertFalse(MPINValidator.validate_mpin_part_a("3097"))
        
    def test_part_b_weak_mpins(self):
        """Test Part B with weak MPINs"""
        # Test common patterns
        self.assertEqual(MPINValidator.validate_mpin_part_b("1234"), "WEAK")
        self.assertEqual(MPINValidator.validate_mpin_part_b("1111"), "WEAK")
        
        # Test demographic patterns
        dob = "02-01-1998"
        spouse_dob = "15-06-1997"
        anniversary = "22-12-2020"
        
        self.assertEqual(MPINValidator.validate_mpin_part_b("0201", dob, spouse_dob, anniversary), "WEAK")
        self.assertEqual(MPINValidator.validate_mpin_part_b("9802", dob, spouse_dob, anniversary), "WEAK")
        self.assertEqual(MPINValidator.validate_mpin_part_b("1506", dob, spouse_dob, anniversary), "WEAK")
        self.assertEqual(MPINValidator.validate_mpin_part_b("2212", dob, spouse_dob, anniversary), "WEAK")
        
    def test_part_b_strong_mpins(self):
        """Test Part B with strong MPINs"""
        dob = "02-01-1998"
        spouse_dob = "15-06-1997"
        anniversary = "22-12-2020"
        
        self.assertEqual(MPINValidator.validate_mpin_part_b("7294", dob, spouse_dob, anniversary), "STRONG")
        self.assertEqual(MPINValidator.validate_mpin_part_b("8156", dob, spouse_dob, anniversary), "STRONG")
        
    def test_part_c_weak_mpins(self):
        """Test Part C with weak MPINs"""
        dob = "02-01-1998"
        spouse_dob = "15-06-1997"
        anniversary = "22-12-2020"
        
        # Common pattern
        result = MPINValidator.validate_mpin_part_c("1234", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("COMMONLY_USED", result.reasons)
        
        # DOB pattern
        result = MPINValidator.validate_mpin_part_c("0201", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("DEMOGRAPHIC_DOB_SELF", result.reasons)
        
        # Spouse DOB pattern
        result = MPINValidator.validate_mpin_part_c("1506", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("DEMOGRAPHIC_DOB_SPOUSE", result.reasons)
        
        # Anniversary pattern
        result = MPINValidator.validate_mpin_part_c("2212", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("DEMOGRAPHIC_ANNIVERSARY", result.reasons)
        
    def test_part_c_strong_mpins(self):
        """Test Part C with strong MPIN"""
        dob = "02-01-1998"
        spouse_dob = "15-06-1997"
        anniversary = "22-12-2020"
        
        result = MPINValidator.validate_mpin_part_c("7294", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "STRONG")
        self.assertEqual(result.reasons, [])
        
    def test_part_d_weak_6digit_mpins(self):
        """Test Part D with weak 6-digit MPINs"""
        dob = "02-01-1998"
        spouse_dob = "15-06-1997"
        anniversary = "22-12-2020"
        
        # Common pattern
        result = MPINValidator.validate_mpin_part_d("123456", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("COMMONLY_USED", result.reasons)
        
        # DOB pattern
        result = MPINValidator.validate_mpin_part_d("020198", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("DEMOGRAPHIC_DOB_SELF", result.reasons)
        
        # Spouse DOB pattern
        result = MPINValidator.validate_mpin_part_d("150697", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("DEMOGRAPHIC_DOB_SPOUSE", result.reasons)
        
        # Anniversary pattern
        result = MPINValidator.validate_mpin_part_d("221220", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "WEAK")
        self.assertIn("DEMOGRAPHIC_ANNIVERSARY", result.reasons)
        
    def test_part_d_strong_6digit_mpins(self):
        """Test Part D with strong 6-digit MPINs"""
        dob = "02-01-1998"
        spouse_dob = "15-06-1997"
        anniversary = "22-12-2020"
        
        result = MPINValidator.validate_mpin_part_d("729438", dob, spouse_dob, anniversary)
        self.assertEqual(result.strength, "STRONG")
        self.assertEqual(result.reasons, [])
        
    def test_input_validation(self):
        """Test input validation"""
        # Test invalid MPIN length
        with self.assertRaises(ValueError):
            MPINValidator.validate_mpin_part_a("123")
        
        with self.assertRaises(ValueError):
            MPINValidator.validate_mpin_part_b("12345")
            
        with self.assertRaises(ValueError):
            MPINValidator.validate_mpin_part_c("123")
            
        with self.assertRaises(ValueError):
            MPINValidator.validate_mpin_part_d("12345")
            
        # Test non-digit MPIN
        with self.assertRaises(ValueError):
            MPINValidator.validate_mpin_part_a("123a")
            
        with self.assertRaises(ValueError):
            MPINValidator.validate_mpin_part_d("12345a")

# Example usage
def example_usage():
    print("MPIN Validator Example Usage")
    print("-" * 30)
    
    # Example 1: Part A
    mpin = "1234"
    result = MPINValidator.validate_mpin_part_a(mpin)
    print(f"Part A - Is MPIN '{mpin}' commonly used? {result}")
    
    # Example 2: Part B
    mpin = "0201"
    dob = "02-01-1998"
    spouse_dob = "15-06-1997"
    anniversary = "22-12-2020"
    result = MPINValidator.validate_mpin_part_b(mpin, dob, spouse_dob, anniversary)
    print(f"Part B - MPIN '{mpin}' strength: {result}")
    
    # Example 3: Part C
    mpin = "0201"
    result = MPINValidator.validate_mpin_part_c(mpin, dob, spouse_dob, anniversary)
    print(f"Part C - MPIN '{mpin}' evaluation: {result}")
    
    # Example 4: Part D (6-digit)
    mpin = "020198"
    result = MPINValidator.validate_mpin_part_d(mpin, dob, spouse_dob, anniversary)
    print(f"Part D - 6-digit MPIN '{mpin}' evaluation: {result}")
    
    # Example 5: Strong MPIN
    mpin = "7294"
    result = MPINValidator.validate_mpin_part_c(mpin, dob, spouse_dob, anniversary)
    print(f"Part C - MPIN '{mpin}' evaluation: {result}")
    
    # Example 6: Strong 6-digit MPIN
    mpin = "729438"
    result = MPINValidator.validate_mpin_part_d(mpin, dob, spouse_dob, anniversary)
    print(f"Part D - 6-digit MPIN '{mpin}' evaluation: {result}")

if __name__ == "__main__":
    # Run tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # Show example usage
    print("\n")
    example_usage()