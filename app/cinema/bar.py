from app.people import customer as client


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: client.Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")

"""
In app/cinema/bar.py, CinemaBar.sell_product should accept product first and then customer as
 per the task description and examples. 
 Update the static method signature to def sell_product(product: str, customer: client.Customer) -> None:
  and adjust any calls (positional or keyword) to match, e.g.,
   sell_product(product=viewer.food, customer=viewer).
"""