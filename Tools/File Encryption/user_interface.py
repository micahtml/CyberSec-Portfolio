import argparse
import pyAesCrypt
from os.path import isfile
from sys import exit
import getpass
import tkinter as tk
from tkinter import filedialog


def select_file():
    file_path = filedialog.askopenfilename()
    # Use the selected file for encryption/decryption?

    maxPassLen = 1024  # maximum password length (number of chars)

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    # parse command line arguments
    parser = argparse.ArgumentParser(description=("Encrypt/decrypt a file "
                                                "using AES256-CBC."))
    parser.add_argument("filename", type=str,
                        help="file to encrypt/decrypt")
    parser.add_argument("-o", "--out", type=str,
                        default=None, help="specify output file")
    parser.add_argument("-p", "--password", type=str,
                        default=None, help="specify the password")

    # encrypt OR decrypt....
    groupED = parser.add_mutually_exclusive_group(required=True)
    groupED.add_argument("-e", "--encrypt",
                        help="encrypt file", action="store_true")
    groupED.add_argument("-d", "--decrypt",
                        help="decrypt file", action="store_true")
    args = parser.parse_args()


    # check for input file existence
    if not isfile(args.filename):
        exit("Error: file \"" + args.filename + "\" was not found.")

    # check if the user has not supplied a password
    if not args.password:
        # prompt the user for password
        passw = str(getpass.getpass("Password:"))
    else:
        # warn the user
        print("Warning: passing passwords as plaintext "
            "command-line arguments may be unsafe.")
        # get the password from the argument
        passw = args.password

    if args.encrypt:
        # check against max password length
        if len(passw) > maxPassLen:
            exit("Error: password is too long")

        # Check password complexity
        # here assume that a good password is at least 8 chars long
        # and includes at least:
        # 1 lowercase char
        # 1 uppercase char
        # 1 digit
        # 1 symbol
        if not ((len(passw) > 7) and any(c.islower() for c in passw)
                and any(c.isupper() for c in passw)
                and any(c.isdigit() for c in passw)
                and any(not (c.isalnum()) for c in passw)):
            print("Warning: your password seems weak.")
            print("A password should be at least 8 chars long and should "
                "contain at least one lowercase char, one uppercase char, "
                "one digit and one symbol.")

        # re-prompt the user for password
        # if it was not supplied from the command line
        if not args.password:
            passwConf = str(getpass.getpass("Confirm password:"))
            # check the second pass against the first
            if passw != passwConf:
                exit("Error: passwords you provided do not match")

        # open output file
        if args.out is not None:
            ofname = args.out
        else:
            ofname = args.filename+".aes"

        # call encryption function
        try:
            pyAesCrypt.encryptFile(args.filename, ofname, passw, bufferSize)
        # handle IO errors
        except IOError as ex:
            exit(ex)
        # handle value errors
        except ValueError as ex:
            exit(ex)

    elif args.decrypt:
        # open output file
        if args.out is not None:
            ofname = args.out
        elif args.filename.endswith(".aes"):
            ofname = args.filename[:-4]
        else:
            exit("Error: if input file extension is not \".aes\", you should "
                "provide the output file name through \"-o\" option.")

        # call decryption function
        try:
            pyAesCrypt.decryptFile(args.filename, ofname, passw, bufferSize)
        # handle IO errors
        except IOError as ex:
            exit(ex)
        # handle value errors
        except ValueError as ex:
            exit(ex)

def encrypt():
    # Perform encryption using selected file and key?
    

def decrypt():
    # Perform decryption using selected file and key

# Example usage:
root = tk.Tk()
button = tk.Button(root, text='Select File', command=select_file)
button.pack()
root.mainloop()
