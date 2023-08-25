import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arguments()
    table = []

    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                table.append(row)
        print(tabulate(table, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_command_line_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def  check_file(file):
    if ".csv" not in file:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
