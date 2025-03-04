'''
write a program to make a copy of text file "this.txt" 

'''
x_content = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique quia, deleniti accusantium nam aliquam non eaque perferendis possimus quas officiis ipsam eos qui inventore culpa sunt fugit. Ut qui fugit porro sed distinctio libero voluptatum cupiditate repellat. Quia aspernatur impedit error amet eum. Quam minima debitis officia optio. Ipsam vitae, natus perspiciatis a ducimus animi eveniet aut commodi placeat ea quis quaerat itaque aspernatur magni ratione facilis quisquam obcaecati odit asperiores fugit in amet cum expedita laboriosam? Autem, vero ut! Quae necessitatibus omnis quam accusamus tenetur praesentium nesciunt perferendis mollitia quo reiciendis voluptas deserunt"



def create_file():
    with open("this.txt", "w") as f:
        f.write(x_content)


def create_copy():
    with open("this.txt", "r") as f:
        words = f.read()

    with open("this_copy.txt", "w") as file:
        file.write(words)



create_file()
create_copy()
