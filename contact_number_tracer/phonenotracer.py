import phonenumbers
from phonenumbers import geocoder, carrier

def track_phone_number(number):
    try:
        # Parse the phone number (Include country code, e.g., +1 for USA)
        parsed_number = phonenumbers.parse(number)

        # Get the General Location (City/State/Country)
        location = geocoder.description_for_number(parsed_number, "en")

        # Get the Service Provider (Carrier)
        service_provider = carrier.name_for_number(parsed_number, "en")

        print(f"Results for {number}:")
        print(f"Location: {location}")
        print(f"Carrier: {service_provider}")
        
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
my_number = "" # replace with the contact number you wanna trace  
track_phone_number(my_number)