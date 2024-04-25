def format_monetary_value(value, unit='international'):
    """
    Formats a monetary value with commas separating thousands and limits fractions to two digits.
    Can switch between Nepali units and International units.

    Args:
        value (float): The monetary value to be formatted.
        unit (str): The unit system to use. Default is 'international'. Set to 'nepali' for Nepali units.

    Returns:
        str: The formatted monetary value.
    """
    # Convert the value to a string
    value_str = str(value)

    # Split the string into integer and fractional parts
    parts = value_str.split('.')

    # Format the integer part with commas separating thousands
    if unit == 'nepali':
        integer_part = '{:,}'.format(int(parts[0])).replace(',', ',')
    else:
        integer_part = '{:,}'.format(int(parts[0]))

    # Get the fractional part and limit it to two digits
    if len(parts) > 1:
        fractional_part = parts[1][:2]
        if fractional_part:
            formatted_value = f"{integer_part}.{fractional_part}"
        else:
            formatted_value = integer_part
    else:
        formatted_value = integer_part

    return formatted_value

# Example usage
value1 = 111625.92822
value2 = 12345678.9012

print(f"International format: {format_monetary_value(value1)}")
print(f"Nepali format: {format_monetary_value(value1, unit='nepali')}")

print(f"\nInternational format: {format_monetary_value(value2)}")
print(f"Nepali format: {format_monetary_value(value2, unit='nepali')}")