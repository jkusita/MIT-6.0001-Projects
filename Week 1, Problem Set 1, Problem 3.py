# s = "azcbobobegghakl"
s = str.lower(input("Enter a string: "))
s_length = len(s)
output_list = []
output_count = []

output_list.append(s[0])

for i in range(s_length):
    try:
        # Keeps on updating the list if the letters are in alpohabetical order using ASCII
        if ord(s[i + 1]) >= ord(s[i]):
            output_list.append(s[i + 1])
            if len(output_count) < len((output_list)):
                output_count = output_list

        # Clears the list if the letters aren't in alphabetical order.
        else:
            output_list = []
            output_list.append(s[i + 1])              
    except IndexError:
        pass

# Converts the list's elements into a string:
print("\n" + "Longest substring in alphabetical order is: " + "".join(output_count) + "\n")
