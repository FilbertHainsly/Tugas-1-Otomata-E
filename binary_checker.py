def is_valid_binary(binary_string, valid_set):
        if binary_string == "":
            return True
        
        for s in valid_set:
            if binary_string.startswith(s):
                if is_valid_binary(binary_string[len(s):], valid_set):  
                    return True
        return False

S = {"00", "10", "010", "01001"}

binary_string = input("Masukkan string biner: ")

if is_valid_binary(binary_string, S):
    print("Valid")
else:
    print("Tidak Valid")