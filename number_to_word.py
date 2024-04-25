def number_to_word(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    def convert_three_digits(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + convert_three_digits(num % 10) if num % 10 else "")
        else:
            return ones[num // 100] + " Hundred" + (" " + convert_three_digits(num % 100) if num % 100 else "")

    num_str = str(num)
    length = len(num_str)
    if length > 12:
        return "Number too large to convert"

    billions = int(num_str[:-9]) if length > 9 else 0
    millions = int(num_str[-9:-6]) if length > 6 else 0
    thousands = int(num_str[-6:-3]) if length > 3 else 0
    hundreds = int(num_str[-3:])

    word = ""
    if billions:
        word += convert_three_digits(billions) + " Billion"
    if millions:
        word += (" " + convert_three_digits(millions) + " Million") if word else convert_three_digits(millions) + " Million"
    if thousands:
        word += (" " + convert_three_digits(thousands) + " Thousand") if word else convert_three_digits(thousands) + " Thousand"
    if hundreds:
        word += (" " + convert_three_digits(hundreds)) if word else convert_three_digits(hundreds)

    return word


user_input = input("Enter a number: ")


try:
    num = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:

    word = number_to_word(num)
    print(f"The word representation of {num} is: {word}")