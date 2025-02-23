#!/usr/bin/env python3
import sys

# Difficulty levels and their respective points
difficulty_levels = {
    "-e": 0.5,  # Easy
    "-m": 1.0,  # Medium
    "-h": 1.5,  # Hard
    "-i": 2.0   # Insane
}

def compare_files(difficulty, file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = set(line.rstrip() for line in f1.readlines())  # Remove trailing spaces
        lines2 = set(line.rstrip() for line in f2.readlines())  # Remove trailing spaces
    
    common_lines = lines1.intersection(lines2)
    identical_lines = len(common_lines)
    total_lines = len(common_lines)  # Ignore extra lines
    points = identical_lines * difficulty_levels[difficulty]  # Assign points based on difficulty level
    
    print(f"Identical lines: {identical_lines} out of {total_lines}")
    print(f"Total points: {points}")
    
    if lines1 == lines2:
        print("The files are identical.")
    else:
        print("Differences found:")
        missing_in_file2 = lines1 - lines2
        missing_in_file1 = lines2 - lines1
        
        if missing_in_file2:
            print("Lines present in first file but missing in second file:")
            for line in missing_in_file2:
                print(line)
        
        if missing_in_file1:
            print("Lines present in second file but missing in first file:")
            for line in missing_in_file1:
                print(line)

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in difficulty_levels:
        print("Usage: comparefiles <-e|-m|-h|-i> <file1> <file2>")
        sys.exit(1)
    compare_files(sys.argv[1], sys.argv[2], sys.argv[3])
