class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    def calculate_sum_and_product(self, a, b):
        sum_result = self.add(a, b)          # Calling static method from an instance method
        product_result = MathHelper.multiply(a, b)  # Calling static method from an instance method
        return sum_result, product_result



def main():
    # Using the instance method to call static methods
    helper = MathHelper()
    sum_result, product_result = helper.calculate_sum_and_product(3, 5)

    print(f"Sum: {sum_result}, Product: {product_result}")

#Execute --> python3 static_methods.py
main()