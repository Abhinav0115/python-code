'''
Write a class Train which has method to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

'''


class Train:
    available = 64
    fair = 101
    totalTicket = 0
    def __init__(self):
        pass

    def book(self, totalCount):
        self.available -= totalCount
        print(f"Train ticket for {totalCount} has been booked. Total fair is {totalCount*self.fair}")

    def get_status(self):
        print(f"Total number of available ticket is {self.available}")

    def get_fair(self, totalcount):
        totalFair = totalcount *self.fair
        print(f"total fair for the {totalcount} tickets is {totalFair}")


book1 = Train()
book1.book(5)
book1.book(5)
book1.get_status()
book1.get_fair(10)
