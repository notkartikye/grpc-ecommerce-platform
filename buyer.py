import grpc

# Import generated proto modules
import market_pb2
import market_pb2_grpc
import uuid
from concurrent import futures
import threading

# Define the buyer client class
class BuyerClient:
    def __init__(self):
        # Establish a gRPC channel and stub
        self.channel = grpc.insecure_channel('34.125.84.69:50051')  # Use the market server address
        self.stub =  market_pb2_grpc.MarketServiceStub(self.channel)


    def search_item(self, item_name, category):
        request = market_pb2.SearchItemRequest(item_name=item_name, category=category)
        response = self.stub.SearchItem(request)

        print("Search results:")
        for item in response.items:
            print("–")
            print(f"Item ID: {item.item_id}")
            print(f"Price: ${item.price}")
            print(f"Name: {item.product_name}")
            print(f"Category: {item.category}")
            print(f"Description: {item.description}")
            print(f"Quantity Remaining: {item.quantity_remaining}")
            print(f"Rating: {item.rating} / 5  |  Seller: {item.seller_address}")
            print("–")


    def buy_item(self, item_id, quantity, buyer_address):
        request =  market_pb2.BuyItemRequest(item_id=item_id, quantity=quantity, buyer_address=buyer_address)
        response = self.stub.BuyItem(request)
        if response.status ==  market_pb2.BuyItemResponse.Status.SUCCESS:
            print("SUCCESS: Item purchased successfully.")
        else:
            print("FAILED: Unable to purchase item. Please try again.")


    def add_to_wishlist(self, item_id, buyer_address):
        request =  market_pb2.AddToWishListRequest(item_id=item_id, buyer_address=buyer_address)
        response = self.stub.AddToWishList(request)
        if response.status ==  market_pb2.AddToWishListResponse.Status.SUCCESS:
            print("SUCCESS: Item added to wishlist successfully.")
        else:
            print("FAILED: Unable to add item to wishlist. Please try again.")


    def rate_item(self, item_id, buyer_address, rating):
        request =  market_pb2.RateItemRequest(item_id=item_id, buyer_address=buyer_address, rating=rating)
        response = self.stub.RateItem(request)
        if response.status ==  market_pb2.RateItemResponse.Status.SUCCESS:
            print("SUCCESS: Item rated successfully.")
        else:
            print("FAILED: Unable to rate item. Please try again.")

    def notify_buyer(self, request, context):
        item_details = request.itemDetails

        print("#######")
        print("The Following Item has been updated:")
        print(f"Item ID: {item_details.item_id}")
        print(f"Price: ${item_details.price}")
        print(f"Name: {item_details.product_name}")
        print(f"Category: {market_pb2.Category.Name(item_details.category)}")
        print(f"Description: {item_details.description}")
        print(f"Quantity Remaining: {item_details.quantityRemaining}")
        print(f"Rating: {item_details.rating:.1f} / 5  |  Seller: {item_details.seller}")
        print("#######")
        return market_pb2.NotifyClientResponse(status=market_pb2.NotifyClientResponse.Status.SUCCESS)
    def BuyerNotification(self, request, context):
        print(request.item)
        return market_pb2.ClientNotificationResponse(message="SUCCESS")

def display_buyer_menu():
    print("Choose an option:")
    print("1. Search Item")
    print("2. Buy Item")
    print("3. Add To Wishlist")
    print("4. Rate Item")
    choice = input("Enter your choice: ")
    return choice

def serve(buyer_address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_BuyerServiceServicer_to_server(BuyerClient(), server)
    server.add_insecure_port(f'[::]:{buyer_address}')  # Use the desired port for your market server
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    buyer_client = BuyerClient()
    port = input("Enter buyer address (port): ")
    ip="34.125.238.148:"
    buyer_address=ip+port
    thread = threading.Thread(target = serve,args=(port,), daemon=True).start()
    while True:
        user_choice = display_buyer_menu()

        if user_choice == '1':
            # Search for an item
            item_name = input("Enter the name of the item you want to search for: ")
            category = input("Enter the category of the item you want to search for (1. ELECTRONICS, 2. CLOTHING, 3. FOOD, 4. ANY): ")
            buyer_client.search_item(item_name, (category))

        elif user_choice == '2':
            # Buy an item
            item_id = int(input("Enter the item ID of the item you want to buy: "))
            quantity = int(input("Enter the quantity you want to buy: "))
            buyer_client.buy_item(item_id, quantity, buyer_address)

        elif user_choice == '3':
            # Add item to wishlist
            item_id = int(input("Enter the item ID of the item you want to add to wishlist: "))
            buyer_client.add_to_wishlist(item_id, buyer_address)

        elif user_choice == '4':
            # Rate an item
            item_id = int(input("Enter the item ID of the item you want to rate: "))
            rating = int(input("Enter the rating you want to give (1-5): "))
            buyer_client.rate_item(item_id, buyer_address, rating)

        elif user_choice == '5':
            # Exit
            break

        else:
            print("Invalid choice. Please try again.")

    # buyer_client.search_item()  # Search for all items
    # # Provide desired parameters for buying an item
    # buyer_client.buy_item(item_id=1, quantity=1, buyer_address="buyer_ip:buyer_port")
    # # Provide desired parameters for adding an item to wishlist
    # buyer_client.add_to_wishlist(item_id=1, buyer_address="buyer_ip:buyer_port")
    # # Provide desired parameters for rating an item
    # buyer_client.rate_item(item_id=1, buyer_address="buyer_ip:buyer_port", rating=5)
