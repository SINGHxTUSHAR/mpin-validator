## This file contains constants used in the application
class Constants:
    # Commonly used 4-digit MPINs
    COMMON_MPINS_4 = [
        "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999",
        "1234", "2345", "3456", "4567", "5678", "6789", "9876", "8765", "7654", "6543", "5432", "4321",
        "1212", "2121", "1122", "2211", "1221", "2112", "0123", "3210",
        "1357", "2468", "1470", "0147", "2580", "0258", "1590", "0159",
        "2580", "0852", "1230", "0123", "9630", "0369", "7410", "0147",
        "0911", "1109", "1001", "2002", "2020", "1919", "2000", "1990", "1980", "1970", "1960", "1950",
        "0101", "0202", "0303", "0404", "0505", "0606", "0707", "0808", "0909"
    ]

    # Commonly used 6-digit MPINs
    COMMON_MPINS_6 = [
        "000000", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999",
        "123456", "234567", "345678", "456789", "987654", "876543", "765432", "654321", "543210", "012345",
        "121212", "212121", "112233", "332211", "112233", "332211", "123123", "321321",
        "135790", "246802", "147036", "147258", "258369", "963852", "159357", "753159",
        "010101", "020202", "030303", "040404", "050505", "060606", "070707", "080808", "090909",
        "198000", "199000", "200000", "201000", "202000", "198500", "199500", "200500", "201500"
    ]

    # Demographic related constants
    DEMOGRAPHIC_DOB_SELF = "DEMOGRAPHIC_DOB_SELF"
    DEMOGRAPHIC_DOB_SPOUSE = "DEMOGRAPHIC_DOB_SPOUSE"
    DEMOGRAPHIC_ANNIVERSARY = "DEMOGRAPHIC_ANNIVERSARY"
    COMMONLY_USED = "COMMONLY_USED"

    # Strength indicators
    STRONG = "STRONG"
    WEAK = "WEAK"