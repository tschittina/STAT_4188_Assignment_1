encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
chars = list(encrypted_message)
n = len(chars)

for x in range(1, n//2, 2):
    y = n - x - 1

    chars[x], chars[y] = chars[y], chars[x]

decrypted_message = ''.join(chars)
print(decrypted_message)