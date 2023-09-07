# Explicit Type Conversion

# Converting string(higher) to integer(lower) datatype.
num_int = 123
num_str = "456"
new_type_2 = num_int+int(num_str)
print("New Data Type:", new_type_2)

# Convert datatype to integer (using "Base"). 
# "Base" specifies the "Base" in which string is if the datatype is if datatype is string.
string = "10010"
print("Converting the datatype to integer base 2:", int(string,2))
