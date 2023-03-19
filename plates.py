plate = ""
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <=6:
        return True
    if s[0].isdigit() or s[1].isdigit():
        return False
  
    number_encountered = False
    for char in s:
        # check If first number it must not be 0
        if char == "0" and number_encountered == False:
            return False
        
        if char.isdigit():
            number_encountered = True
        # chack  letters after numbers
        elif number_encountered:
            return False
    
    return True

main()

 
