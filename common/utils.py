## This file contains utility functions
import datetime
from common.constants import Constants

def generate_date_variants(date_obj):
    """Generate different possible PIN variants from a date"""
    if date_obj is None:
        return []

    variants = []
    
    # Format: DDMM
    variants.append(date_obj.strftime("%d%m"))
    
    # Format: MMDD
    variants.append(date_obj.strftime("%m%d"))
    
    # Format: YYYY
    variants.append(date_obj.strftime("%Y"))
    
    # Format: YY
    variants.append(date_obj.strftime("%y"))
    
    # Format: MMYY 
    variants.append(date_obj.strftime("%m%y"))
    
    # Format: YYMM
    variants.append(date_obj.strftime("%y%m"))
    
    # Format: DDYY
    variants.append(date_obj.strftime("%d%y"))
    
    # Format: YYDD
    variants.append(date_obj.strftime("%y%d"))
    
    # Format: DMYY (without leading zeros)
    day = str(date_obj.day)
    month = str(date_obj.month)
    year_short = date_obj.strftime("%y")
    variants.append(f"{day}{month}{year_short}")
    
    # Format: YYMD (without leading zeros)
    variants.append(f"{year_short}{month}{day}")

    # For 6-digit variants
    # Format: DDMMYY
    variants.append(date_obj.strftime("%d%m%y"))
    
    # Format: YYMMDD
    variants.append(date_obj.strftime("%y%m%d"))
    
    # Format: MMDDYY
    variants.append(date_obj.strftime("%m%d%y"))
    
    # Format: YYDDMM 
    variants.append(date_obj.strftime("%y%d%m"))
    
    # Format: DDMMYYYY
    variants.append(date_obj.strftime("%d%m%Y"))
    
    # Format: MMDDYYYY
    variants.append(date_obj.strftime("%m%d%Y"))
    
    # Reverse of all variants
    reverse_variants = []
    for var in variants:
        reverse_variants.append(var[::-1])
    
    # Add all variants to the result
    variants.extend(reverse_variants)
    
    return variants

def parse_date(date_str):
    """Parse date string in format DD-MM-YYYY"""
    if not date_str:
        return None
    
    try:
        return datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        return None