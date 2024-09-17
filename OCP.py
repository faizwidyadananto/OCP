class DiscountCalculator:
    def get_discount(self, customer_type):
        if customer_type == "regular":
            return 10
        elif customer_type == "vip":
            return 20
        else:
            return 0

# Penggunaan
calculator = DiscountCalculator()
print(calculator.get_discount("regular"))  # Output: 10
print(calculator.get_discount("vip"))      # Output: 20
from abc import ABC, abstractmethod

# Abstraction untuk diskon
class Discount(ABC):
    @abstractmethod
    def get_discount(self):
        pass

# Implementasi diskon untuk pelanggan regular
class RegularDiscount(Discount):
    def get_discount(self):
        return 10

# Implementasi diskon untuk pelanggan VIP
class VipDiscount(Discount):
    def get_discount(self):
        return 20

# Implementasi diskon untuk pelanggan Super VIP
class SuperVipDiscount(Discount):
    def get_discount(self):
        return 30

# Kelas yang menggunakan OCP
class DiscountCalculator:
    def __init__(self, discount: Discount):
        self.discount = discount

    def calculate(self):
        return self.discount.get_discount()

# Penggunaan
regular_discount = RegularDiscount()
vip_discount = VipDiscount()
super_vip_discount = SuperVipDiscount()

# Kalkulasi diskon
calculator = DiscountCalculator(regular_discount)
print(calculator.calculate())  # Output: 10

calculator = DiscountCalculator(vip_discount)
print(calculator.calculate())  # Output: 20

calculator = DiscountCalculator(super_vip_discount)
print(calculator.calculate())  # Output: 30
