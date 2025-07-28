import random
import string


# ? Used lists.
sum_number = []


# ? Information about the composant the Paassword.
print("Welcome to the Password Generator !!")
total_number = int(input("Enter the total number of character in the Password:  "))
letters_number = int(input("Enter the number of letters in the Password:  "))
sum_number.append(letters_number)
numbers_number = int(input("Enter the number of numbers in the Password:  "))
sum_number.append(numbers_number)
symbol_number = int(input("Enter the number of symbols in the Password:  "))
sum_number.append(symbol_number)

# ? التحقق من الشرط و انشاء كلمة السر قوية
if sum(sum_number) == total_number : 
# todo --> OR if (letters_number+numbers_number+symbol_number) == total_number:
    letters = random.choices(string.ascii_letters, k=letters_number)
    
    numbers = random.choices(string.digits, k=numbers_number)
    
    symbols = random.choices(string.punctuation, k=symbol_number)
    
    shuffel_password = letters + numbers + symbols
    
    random.shuffle(shuffel_password)
    print("Generator Password is: ","".join(shuffel_password))

# ? تلف الشرط
else :
    print("Ivalide input!! The sum o letters, numbers and symbols doesn't match the Password")
