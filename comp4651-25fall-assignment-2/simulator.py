import time

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: The file at {file_path} not found.")
    except IOError:
        print(f"Error: IO error while reading the file at {file_path}.")

def main():
    acc = 0

    file_path = 'guest_program.txt'

    lines = read_file(file_path)
    if lines:
        for line in lines:
            if not line:
                continue
            instruction = line.strip().split()

            match instruction[0]:
                case "add":
                    print(f"[Guest] Executing: {instruction[0]} {instruction[1]}")
                    acc += int(instruction[1])
                case "print":
                    print(f"[Guest] Executing: {instruction[0]}")
                    print(f"Accumulator value: {acc}")
                case "scan_disk":
                    print("[VMM] Trapped privileged instruction 'scan_disk', emulating...")
                    # Don't think I should implement scan disk function, so let's imagine it is scanning...
                case "halt":
                    print("[VMM] Trapped privileged instruction 'halt'. Halting guest.")
                    # Using break as a halt, sleep to make sure print shows before break
                    time.sleep(1)
                    break
                case _:
                    print(f"Unknown instruction: {instruction[0]}")

if __name__ == "__main__":
    main()
