import os


def move_file(command: str) -> None:
    try:
        cm, file_input, file_output = command.strip().split(" ")
    except ValueError:
        return
    if cm != "mv":
        return

    if os.path.dirname(file_output) == "":
        os.rename(file_input, file_output)
        return

    file_output_dir = os.path.dirname(file_output)
    file_output_name = os.path.basename(file_output)
    os.makedirs(file_output_dir, exist_ok=True)
    with (open(file_input, "r") as file_in,
          open(os.path.join(file_output_dir, file_output_name), "w")
          as file_out):
        file_out.write(file_in.read())
    os.remove(file_input)
