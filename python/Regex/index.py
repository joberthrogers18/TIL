import re

if __name__ == "__main__":

    pattern = r"Cookie"
    sequence = "Cookie"

    if re.match(pattern, sequence):
        print("Match")
    else:
        print("Not Match!") 


    # period match a single character except the new line 
    print(re.search(r"Co.k.e", "Cookie").group())
    # Check if start with the search character after "^" symbol
    print(re.search(r"^Mean", "Meaning of that word").group())
    # Verify if finish with the word before the "$" symbol and return it in group
    print(re.search(r'cake$', "Cake! Let's eat cake").group())
    #repetition
    print(re.search(r'Co+kie', 'Cooookie').group())
    #repetition number
    print(re.search(r'[0-9]+', '5555 6666').group())
    # Checks for any occurrence of a or o or both in the given sequence
    print(re.search(r'Ca*o*kie', 'Cooookie').group())

    print()

    statement = 'Please contact us at: support@datacamp.com'
    match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
    if statement:
        print("Email address:", match.group()) # The whole matched text
        print("Username:", match.group(1)) # The username (group 1)
        print("Host:", match.group(2)) # The host (group 2)
