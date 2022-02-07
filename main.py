def main():
    # Welcome message
    print(
        "Hello, this program will simplify\nthe process of creating a lot of files with the same name!\nPress any "
        "key to continue...")
    input()

    # Inputting the directory, quantity and name of files
    # === directory ===
    print("Input directory you wish to create files in:", end=' ')
    fileDirectory = str(input())

    # === quantity ===
    print("Input how many files you want to create:", end=' ')
    fileQuantity = int(input())

    # !=! check for validity !=!
    if fileQuantity == 0:
        fileQuantity = 1
    elif fileQuantity < 0:
        fileQuantity = abs(fileQuantity)

    fileQuantity += 1

    # === name ===
    print("Input a name of your file:", end=' ')
    fileName = str(input())

    # === format ===
    print("Input the file's format (for example cpp):", end=' ')
    fileFormat = str(input())

    # === snippets ===
    print("Do you want to create \"Hello, world!\" snippet? (Y/N):", end=' ')
    snippetEnabled = str(input()).lower()

    # Creating files
    for i in range(1, fileQuantity):
        file = open(f"{fileDirectory}/{fileName}{i}.{fileFormat}", "a")

        if (fileFormat == "cpp") and (snippetEnabled == 'y'):
            file.write("#include \"iostream\"\n\nint main(){\n\n\treturn 0;\n}")
        elif (fileFormat == "py") and (snippetEnabled == 'y'):
            file.write("def main():\n\treturn\n\nif __name__ == \'__main__\':\n\tmain()")
        elif (fileFormat == "java") and (snippetEnabled == 'y'):
            file.write("class Main{\n    public static void main(String[] args){\n        System.out.println(\"Hello "
                       "World!\");\n    }\n}")
        elif (fileFormat == "cs") and (snippetEnabled == 'y'):
            file.write("namespace Main\n{\n    class Main{         \n        static void Main(string[] args)\n        "
                       "{\n            System.Console.WriteLine(\"Hello World!\");\n        }\n    }\n}")
        elif (fileFormat == "pde") and (snippetEnabled == 'y'):
            file.write("void setup() {\n  size(640, 360);\n  stroke(255);\n}\n\nvoid draw(){\n  background(0);\n  \n  "
                       "fill(80);\n  noStroke();\n}")
        elif (fileFormat == "c") and (snippetEnabled == 'y'):
            file.write("#include <stdio.h>\n\nint main() {\n   printf(\"Hello, World!\");\n\n   return 0;\n}")
            
        file.close()

    print("Done!\n")

    return


if __name__ == '__main__':
    main()
