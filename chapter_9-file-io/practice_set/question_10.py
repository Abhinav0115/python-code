'''
Write a program to wipe out the content of the file using the python.

'''



def create_file(x_content, file_name):
    with open(f"{file_name}.txt", "w") as f:
        f.write(x_content)


def Wipe_data(file):
        with open(f"{file}.txt", "w") as f:
            f.write("")


x = "hello world, X is new social media, that replaced the twitter."
create_file(x, "z_alpha")
Wipe_data("z_alpha")

