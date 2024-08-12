import sys
import os
from datetime import datetime


def create_dir_and_file() -> None:
    command_from_terminal = sys.argv
    dir_path = ""

    if "-d" in command_from_terminal:
        dir_name = sys.argv.index("-d") + 1
        dir_path = (
            os.path.join
            (*sys.argv
                [dir_name:sys.argv.index("-f")
                    if "-f" in sys.argv else len(sys.argv)])
        )
        os.makedirs(dir_path)

    if "-f" in command_from_terminal:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        file_path = os.path.join(dir_path, filename) if dir_path else filename

        with open(file_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}\n")
            line_number = 1

            while True:
                content = input(f"Enter line {line_number}: ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1


if __name__ == "__main__":
    create_dir_and_file()
