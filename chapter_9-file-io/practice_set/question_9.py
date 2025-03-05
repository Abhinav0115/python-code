'''
Write a program to find out the whether the file is identicals and matches the content of the another file

'''



def create_file(x_content, file_name):
    with open(f"{file_name}.txt", "w") as f:
        f.write(x_content)


def find_identical(file_1, file_2):
    with open(f"{file_1}.txt", "r") as f1:
        content_1 = f1.read()

    with open(f"{file_2}.txt", "r") as f2:
        content_2 = f2.read()
    

    if (content_1 == content_2):
        print("The files are identical")
    else:
        print("The files are not identical")



x = "hello world, X is new social media, that replaced the twitter."
Y = "hello world, X is new social media."
create_file(x, "z_alpha_1")
create_file(Y, "z_alpha_2")

find_identical("z_alpha_1", "z_alpha_2")

