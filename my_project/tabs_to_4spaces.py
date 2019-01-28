"""Python program to convert tabs in a text file (python script) into 4 spaces.
It take a file name or path from the user.
If the user enters the path without file name the code searches the path for all script files and corrects them.
If not it only corrects the given file."""

import glob

def main():
    """The main operation is done by this function and by means of an entry point, a command is defined for it"""
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
        except IsADirectoryError: #If the user enters a path without file name
            search_str = file_name + "/**/*.py"
            for file in glob.glob(search_str, recursive = True):
                f = open(file, "r")
                file_contents = f.read()
                new_contents = file_contents.replace("	", "    ")
                f.close()
                if (file_contents != new_contents):
                    f = open(file, "w")
                    f.write(new_contents)
                    f.close
            exit()
        break #If the file name and address is valid
    str = f.read()
    f.close()
    str2 = str.replace("****","    ")
    f = open(file_name,"w")
    f.write(str2)
    f.close()

