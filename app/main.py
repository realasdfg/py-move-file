import os


def move_file(command: str) -> None:
    try:
        cm, file_input, file_output = command.strip().split(" ")
    except ValueError:
        return

    file_output_split = file_output.split("/")
    if len(file_output_split) == 1:
        os.rename(file_input, file_output_split[0])
        return

    file_output_name = file_output_split[-1]
    file_output_dir = file_output.replace(file_output_name, "")
    os.makedirs(file_output_dir, exist_ok=True)
    with open(file_input, "r") as file_in, open(file_output, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(file_input)
