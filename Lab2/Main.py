from Scanner import Scanner

if __name__ == "__main__":
    scanner = Scanner()
    tokens = scanner.readFile("p1.txt")

    scanner.populatePifFile()

