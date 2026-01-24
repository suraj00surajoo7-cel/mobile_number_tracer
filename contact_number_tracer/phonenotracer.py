import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests

def get_phone_info(phone_number):
    """
    Get legal information about a phone number including:
    - Validity
    - Geographic region
    - Carrier
    - Timezone
    - Basic number formatting
    """
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        if not phonenumbers.is_valid_number(parsed_number):
            return {"error": "Invalid phone number"}
        
        info = {
            "number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "region": geocoder.description_for_number(parsed_number, "en"),
            "carrier": carrier.name_for_number(parsed_number, "en"),
            "timezone": timezone.time_zones_for_number(parsed_number),
            "number_type": phonenumbers.number_type(parsed_number)  # MOBILE, FIXED_LINE, etc.
        }
        
        return info
        
    except phonenumbers.NumberParseException as e:
        return {"error": str(e)}

def format_results(info):
    """Format the information in a user-friendly way"""
    if "error" in info:
        return f"Error: {info['error']}"
    
    result = [
        f"📱 Phone Information for {info['number']}",
        f"📍 Region: {info['region']}",
        f"📶 Carrier: {info['carrier']}",
        f"⏰ Timezone: {', '.join(info['timezone'])}",
        f"🔢 Type: {get_number_type(info['number_type'])}"
    ]
    
    return "\n".join(result)

def get_number_type(num_type):
    """Convert numeric type to human-readable string"""
    types = {
        0: "Fixed line",
        1: "Mobile",
        2: "Fixed line or mobile",
        3: "Toll free",
        4: "Premium rate",
        5: "Shared cost",
        6: "VoIP",
        7: "Personal number",
        8: "Pager",
        9: "UAN",
        10: "Unknown"
    }
    return types.get(num_type, "Unknown")

if __name__ == "__main__":
    print("Phone Number Tracer - Legal Information Only")
    print("Enter phone number in international format (+[country code][number]):")
    phone = input("> ")
    
    info = get_phone_info(phone)
    print("\n" + format_results(info))
