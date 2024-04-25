def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if any(char.isdigit() for char in string1) or any(char.isdigit() for char in string2):
        return "Numbers are not accepted."

    string1 = ''.join(char for char in string1 if char.isalnum())
    string2 = ''.join(char for char in string2 if char.isalnum())

    if len(string1) != len(string2):
        return False

    frequency1 = {}
    frequency2 = {}

    for char in string1:
        frequency1[char] = frequency1.get(char, 0) + 1
    for char in string2:
        frequency2[char] = frequency2.get(char, 0) + 1

    return frequency1 == frequency2


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = are_anagrams(string1, string2)
if isinstance(result, str):
    print(result)
elif result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")