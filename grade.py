import os
from subprocess import run, Popen, PIPE


def remove_main(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file: {e.filename} - {e.strerror}")


def compile_and_run_java(java_file):
    # Compile the Java file

    run(['javac', java_file])

    # Get the class name by removing the file extension
    class_name = java_file.rsplit('.', 1)[0]

    # Run the Java program and pass input
    process = Popen(
        ['java', class_name], 
        stdin=PIPE, 
        stdout=PIPE, 
        stderr=PIPE, 
        text=True)
    inputs = "5\n4\n10\n"


    try:
        stdout, stderr = process.communicate(inputs)
        stderr = stderr.strip() if stderr is not None else ""
        
    except Exception as e:
        print("Exception:", str(e))
        stdout = ""
        stderr = ""

    # # Print the output and error messages

    expected_output = """Please enter the width of the square: Please enter the width of the rectangle: Please enter the height of the rectangle: The area of the square with a width of 5 is 25.
The area of the rectangle with a width of 4 and the height of 10 is 40.
"""

    stdout_lines = stdout.splitlines()
    expected_output_lines = expected_output.splitlines()


    if(stdout_lines == expected_output_lines):
        print("Well done!")
        remove_main("Main.class")
    else:
        print("Work again")
        remove_main("Main.class")


    if stderr:
        print("Error:")
        print(stderr)
        remove_main("Main.class")

# Specify the path to your Java file
java_file_path = "Main.java"


# Call the function to compile and run the Java file
compile_and_run_java(java_file_path)