from app.people import customer as client


class CinemaBar:

    @staticmethod
    def sell_product(customer: client.Customer , product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
