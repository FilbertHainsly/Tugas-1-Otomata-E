def is_valid_binary(binary_string, valid_set):

    if binary_string == "":
        return True  # Jika string kosong (λ), maka valid
    
    for s in valid_set:
        if binary_string.startswith(s):         
            if is_valid_binary(binary_string[len(s):], valid_set): # Rekursi dengan menghapus bagian yang cocok dari binary_string
                return True
    
    return False  # Jika tidak bisa dipecah sesuai S*, maka tidak valid

# Himpunan S dalam ppt
S = {"00", "10", "010", "01001"}

binary_string = input("Masukkan nilai biner: ")

if is_valid_binary(binary_string, S):
    print("Valid")
else:
    print("Not Valid")
