'''
Write a program to mine a log file and find out whether the log file has "python" in it or not.
'''

content = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique quia, deleniti accusantium nam aliquam non eaque perferendis possimus quas officiis ipsam eos qui inventore culpa sunt fugit. Ut qui fugit porro sed distinctio libero voluptatum cupiditate repellat. Quia aspernatur impedit error amet eum. Quam minima debitis officia optio. Ipsam vitae, natus perspiciatis a ducimus animi eveniet aut commodi placeat ea quis quaerat itaque aspernatur magni ratione facilis quisquam obcaecati odit asperiores fugit in amet cum expedita laboriosam? Autem, vero ut! Quae necessitatibus omnis quam accusamus tenetur praesentium nesciunt perferendis mollitia quo reiciendis voluptas deserunt, vitae veniam aliquid! Officia consequuntur, quam fugiat voluptatibus voluptatem, laborum incidunt optio doloremque dolore doloribus assumenda commodi culpa quia veniam ab adipisci repellendus facilis illo explicabo. Ex delectus ab error tempora ipsam esse quasi, laboriosam dolore ipsum tenetur molestiae molestias consectetur omnis officiis dolor? Reprehenderit fugit nisi consectetur quam. Eligendi, modi. Quam vel voluptatem est. Consequatur reiciendis quia exercitationem aliquid cumque magnam temporibus mollitia alias quae, unde accusamus laboriosam ipsum fugit iusto ex animi quis doloribus voluptatem voluptatibus python? Tempore ipsa animi distinctio repellendus laudantium voluptatum, quibusdam provident, ut quam quos accusantium eveniet laborum enim voluptas eligendi temporibus blanditiis, odio obcaecati! Beatae dignissimos velit laboriosam eaque voluptatibus iure maiores consequuntur tempore nemo sed cupiditate, impedit vitae a aliquid est laudantium ipsum doloremque consectetur facilis sapiente aperiam quos expedita. Voluptatibus optio quas est corporis consequuntur praesentium, consectetur quisquam obcaecati provident nobis, veniam tempore tempora. Id qui corporis quia quasi corrupti asperiores facilis?"


def create_file():
    with open("log.txt", "w") as f:
        f.write(content)



def find_the_word(word_to_find):
    with open("log.txt", "r") as f:
        content = f.read()
    if (word_to_find in content):
        print(f"Yes, the log file has '{word_to_find}' in it.")
    else:
        print(f"No, the log file does not have '{word_to_find}' in it.")



create_file()
find_the_word("python")