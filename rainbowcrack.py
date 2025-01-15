import os

def automate_rainbowcrack(hash_value):
    command = f"rcrack . -h {hash_value}"
    os.system(command)

if __name__ == "__main__":
    hash_value = input("Enter the hash to crack: ")
    automate_rainbowcrack(hash_value)
