alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
#should add lines 8/10 after line 3
direction = True
if direction != "encode" or "decode":
    direction = False
    print(f"You have not written properly 'encode' or 'decode' word! Try again.")   

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            end_text += alphabet[new_position]    
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")    
    return
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

