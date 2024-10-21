# File: ReadFile.py

# Description: This script reads the catalog file `bsc5.dat`, processes the data, 
#              and converts it to a comma-delimited CSV file (`bsc5.csv`).

# Name: Dylan Lam

# UT EID: DXL85

# Date: 10/21/2024
import csv
import sys

def parse_line(line):
    # Extract fields based on character positions
    fields = [
        line[0:4].strip(),    # HR
        line[4:14].strip(),   # Name
        line[14:25].strip(),  # DM
        line[25:31].strip(),  # HD
        line[31:37].strip(),  # SAO
        line[37:41].strip(),  # FK5
        line[41:42].strip(),  # IRflag
        line[42:43].strip(),  # r_IRflag
        line[43:44].strip(),  # Multiple
        line[90:96].strip(),  # GLON (degrees)
        line[96:102].strip(),  # GLAT (degrees)
        line[127:147].strip(), # SpType
        line[75:77].strip(),   # RAh
        line[77:79].strip(),   # RAm
        line[79:83].strip(),   # RAs
        line[83:84].strip(),   # DE-
        line[84:86].strip(),   # DEd
        line[86:88].strip(),   # DEm
        line[88:90].strip(),   # DEs
    ]
    return fields

def convert_to_csv(output_file):
    headers = [
        'HR', 'Name', 'DM', 'HD', 'SAO', 'FK5', 'IRflag', 'r_IRflag', 
        'Multiple', 'GLON', 'GLAT', 'SpType', 'RAh', 'RAm', 'RAs', 
        'DE-', 'DEd', 'DEm', 'DEs'
    ]
    
    try:
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)  
            
            line_count = 0
            for line in sys.stdin:
                if line.strip(): 
                    parsed_data = parse_line(line)
                    writer.writerow(parsed_data)
                    line_count += 1
            print(f"Finished processing {line_count} lines.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    output_file = 'bsc5.csv' 
    convert_to_csv(output_file)
    print(f"Successfully converted input to {output_file}.")

if __name__ == "__main__":
    main()
