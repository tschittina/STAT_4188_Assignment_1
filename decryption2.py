encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
chars = list(encrypted_message)
n = len(chars)

for index in range(1, n//2, 2):
    opp_index = n - index - 1

    chars[index], chars[opp_index] = chars[opp_index], chars[index]

decrypted_message = ''.join(chars)
print(decrypted_message)