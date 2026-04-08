"""
This program converts numbers into their English word representation.
It handles numbers up to trillions and properly mentions scale words
like 'Hundred', 'Thousand', 'Million', 'Billion', etc.
"""

# Dictionary for single digits (0-9)
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# Dictionary for teens (10-19)
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
         "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

# Dictionary for tens place (20, 30, 40, ..., 90)
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

# Dictionary for scale words (Thousand, Million, Billion, Trillion)
scales = ["", "Thousand", "Million", "Billion", "Trillion"]

def convert_hundreds(num):
    """
    Convert a number from 0-999 to English words.
    This handles the hundreds place and the tens/ones places.
    
    Args:
        num (int): A number between 0 and 999
    
    Returns:
        str: The English word representation of the number
    
    Example:
        convert_hundreds(456) -> "Four Hundred Fifty Six"
        convert_hundreds(12) -> "Twelve"
        convert_hundreds(5) -> "Five"
    """
    result = ""
    
    # Handle the HUNDREDS place (e.g., 400, 500, 600)
    if num >= 100:
        result += ones[num // 100] + " Hundred"
        num %= 100  # Keep only the remaining two digits
    
    # If there are remaining digits after hundreds, add a space
    if num > 0:
        if result:  # If we already have hundreds, add a space
            result += " "
        
        # Handle the TENS and ONES places
        if num >= 20:
            # For numbers 20-99
            result += tens[num // 10]  # Add the tens word (Twenty, Thirty, etc.)
            if num % 10 > 0:  # If there's a ones digit
                result += " " + ones[num % 10]
        elif num >= 10:
            # For numbers 10-19 (teens)
            result += teens[num - 10]
        else:
            # For numbers 1-9
            result += ones[num]
    
    return result

def number_to_words(num):
    """
    Convert any integer to its complete English word representation.
    This function handles numbers up to trillions and properly
    mentions scale words (Hundred, Thousand, Million, Billion, Trillion).
    
    Args:
        num (int): The number to convert
    
    Returns:
        str: The complete English word representation with scale words
    
    Examples:
        number_to_words(0) -> "Zero"
        number_to_words(5) -> "Five"
        number_to_words(100) -> "One Hundred"
        number_to_words(1234) -> "One Thousand Two Hundred Thirty Four"
        number_to_words(1000000) -> "One Million"
        number_to_words(1234567890) -> "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety"
    """
    
    # Special case: if the number is zero, return "Zero"
    if num == 0:
        return "Zero"
    
    # Handle negative numbers by recursively calling the function
    # and adding "Negative" prefix
    if num < 0:
        return "Negative " + number_to_words(-num)
    
    # Split the number into groups of three digits (from right to left)
    # Example: 1234567 becomes [567, 234, 1]
    groups = []
    while num > 0:
        groups.append(num % 1000)  # Extract the last three digits
        num //= 1000  # Remove the last three digits from the number
    
    # Reverse the groups so we process from left to right (largest to smallest)
    groups.reverse()
    
    # Convert each group to words and add the appropriate scale word
    result = []
    for i in range(len(groups)):
        if groups[i] > 0:  # Only process non-zero groups
            # Convert the group (0-999) to words
            group_words = convert_hundreds(groups[i])
            
            # Calculate which scale word to add (Thousand, Million, Billion, etc.)
            scale_index = len(groups) - 1 - i
            
            # Add the scale word if needed (skip if scale_index is 0)
            if scale_index > 0:
                group_words += " " + scales[scale_index]
            
            result.append(group_words)
    
    # Join all groups with spaces and return the final result
    return " ".join(result)

# Main program execution
if __name__ == "__main__":
    print("=" * 70)
    print("NUMBER TO ENGLISH WORDS CONVERTER")
    print("=" * 70)
    print("\nThis program converts numbers to their English word representation")
    print("and properly mentions scale words (Hundred, Thousand, Million, etc.)\n")
    
    # Test cases to demonstrate the converter
    test_numbers = [
        0,              # Zero
        5,              # Single digit
        12,             # Teens
        25,             # Two digits
        100,            # One Hundred
        123,            # Hundred with tens and ones
        1000,           # One Thousand
        1234,           # Thousand with more digits
        100000,         # One Hundred Thousand
        1000000,        # One Million
        1234567,        # Million with more digits
        1000000000,     # One Billion
        1234567890,     # Billion with more digits
        999999999999,   # Nearly one trillion
    ]
    
    print("EXAMPLE CONVERSIONS:")
    print("-" * 70)
    
    for num in test_numbers:
        converted = number_to_words(num)
        print(f"{num:>15,} -> {converted}")
    
    # Interactive mode for user input
    print("\n" + "=" * 70)
    print("INTERACTIVE MODE")
    print("=" * 70)
    print("\nEnter a number to convert (or type 'quit' to exit):\n")
    
    while True:
        try:
            user_input = input("Enter a number: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() == 'quit':
                print("\nThank you for using the converter! Goodbye!")
                break
            
            # Convert string input to integer
            number = int(user_input)
            
            # Convert and display the result
            result = number_to_words(number)
            print(f"Result: {result}\n")
            
        except ValueError:
            # Handle invalid input
            print("Invalid input! Please enter a valid integer.\n")