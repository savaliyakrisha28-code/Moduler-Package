def create_file(filename):

    try:
        with open(filename, "x") as file:
            return "File created successfully!"

    except FileExistsError:
        return "File already exists."


def write_file(filename, data):

    try:
        with open(filename, "w") as file:
            file.write(data)

        return "Data written successfully!"

    except OSError as e:
        return f"Error: {e}"


def read_file(filename):

    try:
        with open(filename, "r") as file:
            content = file.read()

        return "File Content:\n" + content

    except FileNotFoundError:
        return "File not found."


def append_file(filename, data):

    try:
        with open(filename, "a") as file:
            file.write(data + "\n")

        return "Data appended successfully!"

    except OSError as e:
        return f"Error: {e}"