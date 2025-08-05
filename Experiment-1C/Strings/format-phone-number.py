#Format Phone Number 1234567890 → (123) 456-7890. Converts a string of 10 digits into the format (XXX) XXX-XXXX

def format(phone):
    if len(phone) != 10 or not phone.isdigit():
        return "Enter exactly 10 digits."
    
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

phone_number = input("Enter a 10-digit phone number: ")
formatted = format(phone_number)
print("Formatted Phone Number:", formatted)
