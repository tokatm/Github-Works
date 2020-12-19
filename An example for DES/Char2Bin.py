plaintext = "CalmDown"
key = "CRYPTOEN"

result_P = ''.join(format(ord(i), 'b') for i in plaintext)
result_K = ''.join(format(ord(i), 'b') for i in key)

print("Result of Plainext Conversion: " + str(result_P))
print("Result of Key Conversion: " + str(result_K))