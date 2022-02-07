import os


def main():
    # Welcome message
    print("Hello, this programm will simplify\nthe process of creating a lot of files with the same name!\nPress any key to continue...")
    input()

    # Inputting the directory, quantity and name of files
    # === directory ===
    print("Input directory you wish to create files in:", end = ' ')
    directory = str(input())

    # === quantity ===
    print("Input how many files you want to create:", end = ' ')
    quantity = int(input())

    # !=! check for validity !=!
    if(quantity == 0):
        quantity = 1
    elif(quantity < 0):
        quantity = abs(quantity)

    # === name ===
    print("Input a name of your file:", end = ' ')
    name = str(input())

    # === format ===
    print("Input the file's format (for example cpp):", end=' ')
    format = str(input())

    # Changing directory to the given one
    os.system(f"cd {directory}")

    # Creating files
    for i in range(1, quantity + 1):
        file = open(f"{directory}/{name}{i}.{format}", "a")

        if(format == "cpp"):
            file.write("#include \"iostream\"\n\nint main(){\n\n\treturn 0;\n}")

        file.close()

    print("Done!\n")

    return

if __name__ == '__main__':
    main()
