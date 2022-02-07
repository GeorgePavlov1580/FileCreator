def main():
    # Welcome message
    print(
        "Hello, this program will simplify\nthe process of creating a lot of files with the same name!\nPress any "
        "key to continue...") 
    input()

    # Inputting the directory, quantity and name of files
    # === directory ===
    print("Input directory you wish to create files in:", end=' ')
    directory = str(input())

    # === quantity ===
    print("Input how many files you want to create:", end=' ')
    quantity = int(input())
    quantity += 1

    # !=! check for validity !=!
    if quantity == 0:
        quantity = 1
    elif quantity < 0:
        quantity = abs(quantity)

    # === name ===
    print("Input a name of your file:", end=' ')
    name = str(input())

    # === format ===
    print("Input the file's format (for example cpp):", end=' ')
    fileFormat = str(input())

    # === snippets ===
    print("Do you want to create \"Hello, world!\" snippet? (Y/N):", end=' ')
    snippet = str(input()).lower()

    # Creating files
    for i in range(1, quantity):
        file = open(f"{directory}/{name}{i}.{fileFormat}", "a")

        if (fileFormat == "cpp") and (snippet == 'y'):
            file.write("#include \"iostream\"\n\nint main(){\n\n\treturn 0;\n}")
        elif (fileFormat == "py") and (snippet == 'y'):
            file.write("def main():\n\treturn\n\nif __name__ == \'__main__\':\n\tmain()")
        elif (fileFormat == "java") and (snippet == 'y'):
            file.write("class Main{\n    public static void main(String[] args){\n        System.out.println(\"Hello "
                       "World!\");\n    }\n}")
        elif (fileFormat == "cs") and (snippet == 'y'):
            file.write("namespace Main\n{\n    class Main{         \n        static void Main(string[] args)\n        "
                       "{\n            System.Console.WriteLine(\"Hello World!\");\n        }\n    }\n}")

        file.close()

    print("Done!\n")

    return


if __name__ == '__main__':
    main()
