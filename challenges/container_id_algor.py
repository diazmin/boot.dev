'''
This algotithm is based on the ISO 6346 standard 
used to calculate the check digit for shipping container IDs.
'''

def calculations(container_id):
    letters_values = (("A", 10),
                      ("B", 12),
                      ("C", 13),
                      ("D", 14),
                      ("E", 15),
                      ("F", 16),
                      ("G", 17),
                      ("H", 18),
                      ("I", 19),
                      ("J", 20),
                      ("K", 21),
                      ("L", 23),
                      ("M", 24),
                      ("N", 25),
                      ("O", 26),
                      ("P", 27),
                      ("Q", 28),
                      ("R", 29),
                      ("S", 30),
                      ("T", 31),
                      ("U", 32),
                      ("V", 34),
                      ("W", 35),
                      ("X", 36),
                      ("Y", 37),
                      ("Z", 38)
                      )
    letters = container_id[:4]
    numbers = container_id[4:]
    replaced_letters = []

    for l in letters:
        for letter, value in letters_values:
            if l == letter:
                replaced_letters.append(value)

    # Completing full string with numbers
    for i in numbers:
        replaced_letters.append(int(i))
    print(replaced_letters)

    # Weight each character by powers of 2 based on its position:
    sum_numbers = 0
    check_digit = 0
    for i in range(0, len(replaced_letters)):
        sum_numbers += replaced_letters[i] * pow(2, i)
    
    check_digit = sum_numbers % 11
    #if check_digit == 10:
     #   check_digit = 0
    
    print(check_digit)
    

calculations("ABCU1000080")