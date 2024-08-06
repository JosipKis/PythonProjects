import csv
import re


def parse_txt_file(txt_file_path):
    data = []

    with open(txt_file_path, 'r') as file:
        content = file.read()

    matches = re.findall(r'Name:\s*(\S+)\s*Address:\s*(\S+)', content, re.MULTILINE)

    for match in matches:
        name, address = match
        data.append((name, address))

    return data


def write_to_csv(csv_file_path, data):
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address'])
        writer.writerows(data)


def main():
    txt_file_path = 'nslookup_results.txt'
    csv_file_path = 'output.csv'

    data = parse_txt_file(txt_file_path)

    write_to_csv(csv_file_path, data)
    print(f"Data has been written to {csv_file_path}")


if __name__ == "__main__":
    main()
