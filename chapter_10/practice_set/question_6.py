'''
Can you chnage the self-paramater inside a class to do something else (say 'self' to 'slf')? Try and report the result.


ans: Yes, we can change the self-paramater inside a class to do something else (say 'self' to 'slf'). 
But it is not a good practice to change the self-paramater to something else.
'''


class Demo:
    msg = "hello"

    def __init__(asdfg, new_msg):
        asdfg.msg = new_msg

    def greet(slf, user):
        print(f" {slf.msg}, {user}")
    
    def Hello(ASDSDF, user):
        print(f" {ASDSDF.msg}, {user}")

d1 = Demo("good morning")
d1.greet("ram")
d1.Hello("raman")
