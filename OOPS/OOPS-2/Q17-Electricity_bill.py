# 17. Electricity Bill System
# Problem

# Generate electricity bill.

# Requirements

# Consumer should contain:

# consumer id
# units consumed
# Functionalities
# Calculate bill
# Add surcharge using static method
# Display bill summary






class Consumer:
    def __init__(self, consumer_id, units_consumed):
        self.__consumer_id = consumer_id
        self.__units_consumed = units_consumed

    def calculate_bill(self):
        if self.__units_consumed <= 100:
            bill = self.__units_consumed * 5
        elif self.__units_consumed <= 200:
            bill = (100 * 5) + ((self.__units_consumed - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((self.__units_consumed - 200) * 10)

        return bill

    @staticmethod
    def add_surcharge(bill):
        surcharge = bill * 0.05
        return surcharge

    def display_bill(self):
        bill = self.calculate_bill()
        surcharge = Consumer.add_surcharge(bill)
        total_bill = bill + surcharge

        print("\n----- Electricity Bill Summary -----")
        print("Consumer ID:", self.__consumer_id)
        print("Units Consumed:", self.__units_consumed)
        print("Electricity Bill: ₹", bill)
        print("Surcharge (5%): ₹", surcharge)
        print("Total Bill: ₹", total_bill)



c1 = Consumer("C101", 150)
c2 = Consumer("C102", 250)


c1.display_bill()
c2.display_bill()
