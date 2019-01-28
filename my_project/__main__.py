#by means of this acript we create a python application

def main():
    """The main routin"""
    while True:
        try:
            file_name = input("Enter a valid file name and address or Press Ctrl+C to exit:") #Getting the file name from the user
            f = open(file_name,"r")
        except KeyboardInterrupt: #If the user presses Ctrl+C
            print("\nYou pressed Ctrl+C")
            exit()
        except FileNotFoundError: #If the file name or address is invlaid
            print("File name or address is invalid")
            continue
        break #If the file name and address is valid
    str = f.read()
    f.close()
    str2 = str.replace("****","    ")
    f = open(file_name,"w")
    f.write(str2)
    f.close()

if __name__ == "__main__":
    main()
