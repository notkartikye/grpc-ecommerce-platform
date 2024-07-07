import grpc

# Import generated proto modules
import market_pb2
import market_pb2_grpc

import uuid
import threading
from concurrent import futures
# Define the seller client class
class SellerClient:
    def __init__(self):
        # Establish a gRPC channel and stub
        self.channel = grpc.insecure_channel('34.125.84.69:50051')  # Use the market server address
        self.stub = market_pb2_grpc.MarketServiceStub(self.channel)
        self.uuid=str(uuid.uuid1())

    def register_seller(self, address):
        # Generate a unique UUID for the seller
        
        print(f"Generated UUID for {address}: {self.uuid}")

        request = market_pb2.RegisterSellerRequest(address=address, uuid=self.uuid)
        response = self.stub.RegisterSeller(request)

        if response.status == market_pb2.RegisterSellerResponse.Status.SUCCESS:
            print("SUCCESS: Seller registered successfully.")
        else:
            print("FAILED: Seller registration failed. Please try again.")

    
    def sell_item(self, product_name, category, quantity, description, seller_address, price_per_unit):
        request = market_pb2.SellItemRequest(
            product_name=product_name,
            category=category,
            quantity=quantity,
            description=description,
            seller_address=seller_address,
            seller_uuid=self.uuid,
            price_per_unit=price_per_unit
        )
        response = self.stub.SellItem(request)
        if response.message == "SUCCESS":
            print("SUCCESS: Item posted for sale successfully.")
            print("Item ID:", response.item_id)
        else:
            print("FAILED: Unable to post item for sale. Please try again.")

    def update_item(self, item_id, new_price, new_quantity, seller_address):
        request = market_pb2.UpdateItemRequest(
            item_id=item_id,
            new_price=new_price,
            new_quantity=new_quantity,
            seller_address=seller_address,
            seller_uuid=self.uuid
        )
        response = self.stub.UpdateItem(request)
        if response.status == market_pb2.UpdateItemResponse.Status.SUCCESS:
            print("SUCCESS: Item updated successfully.")
        else:

            print("FAILED: Unable to update item. Please try again.")

    def delete_item(self, item_id, seller_address):
        request = market_pb2.DeleteItemRequest(
            item_id=item_id,
            seller_address=seller_address,
            seller_uuid=self.uuid
        )
        response = self.stub.DeleteItem(request)
        if response.status == market_pb2.DeleteItemResponse.Status.SUCCESS:
            print("SUCCESS: Item deleted successfully.")
        else:
            print("FAILED: Unable to delete item. Please try again.")

    def display_seller_items(self, seller_address):
        request = market_pb2.DisplaySellerItemsRequest(
            seller_address=seller_address,
            seller_uuid=self.uuid
        )
        response = self.stub.DisplaySellerItems(request)
        print("Your items for sale:")
        for item in response.items:
            print(f"Item ID: {item.item_id}, Price: ${item.price}, Name: {item.product_name}, Category: {item.category}, Description: {item.description},Seller:{item.seller}, Quantity Remaining: {item.quantity_remaining}, Rating: {item.rating}")

    def SellerNotification(self, request, context):
        print(request.item)      
        return market_pb2.SellerNotificationResponse(message="SUCCESS")  
    
    


def display_seller_menu():
    print("Choose an option:")
    print("1. Register Seller")
    print("2. Sell Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Display Seller Items")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

def serve(seller_address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_SellerServiceServicer_to_server(SellerClient(), server)
    server.add_insecure_port(f'[::]:{seller_address}')  # Use the desired port for your market server
    server.start()
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    seller_client = SellerClient()
    port = input("Enter seller address (port): ")
    ip="34.16.176.150:"
    seller_address=ip+port
    thread = threading.Thread(target = serve,args=(port,), daemon=True).start()

    while True:
        user_choice = display_seller_menu()

        if user_choice == '1':
            # Register Seller
            address = input("Enter seller address (port): ")
            seller_client.register_seller(ip+address)

        elif user_choice == '2':
            # Sell Item
            product_name = input("Enter product name: ")
            category = input("Enter category (ELECTRONICS, FASHION, OTHERS): ")
            quantity = int(input("Enter quantity: "))
            description = input("Enter description: ")
            seller_address = input("Enter seller address (port): ")
            
            price_per_unit = float(input("Enter price per unit: "))
            seller_client.sell_item(product_name, category, quantity, description, ip+seller_address, price_per_unit)

        elif user_choice == '3':
            # Update Item
            item_id = int(input("Enter item ID to update: "))
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            seller_address = input("Enter seller address (port): ")
            
            seller_client.update_item(item_id, new_price, new_quantity, ip+seller_address)

        elif user_choice == '4':
            # Delete Item
            item_id = int(input("Enter item ID to delete: "))
            seller_address = input("Enter seller address (port): ")
            seller_client.delete_item(item_id, ip+seller_address)

        elif user_choice == '5':
            # Display Seller Items
            seller_address = input("Enter seller address (port): ")
            
            seller_client.display_seller_items(ip+seller_address)

        elif user_choice == '6':
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


    # # Provide desired parameters for registering as a seller
    # seller_client.register_seller(address="seller_ip:seller_port", uuid="987a515c-a6e5-11ed-906b-76aef1e817c5")
    # # Provide desired parameters for selling an item
    # seller_client.sell_item(product_name="iPhone", category=market_pb2.SellItemRequest.ELECTRONICS, quantity=10, description="This is iPhone 15.", seller_address="seller_ip:seller_port", seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5", price_per_unit=500)
    # # Provide desired parameters for updating an item
    # seller_client.update_item(item_id=123, new_price=600, new_quantity=8, seller_address="seller_ip:seller_port", seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5")
    # # Provide desired parameters for deleting an item
    # seller_client.delete_item(item_id=123, seller_address="seller_ip:seller_port", seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5")
    # # Provide desired parameters for displaying seller items
    # seller_client.display_seller_items(seller_address="seller_ip:seller_port", seller_uuid="987a515c-a6e5-11ed-906b-76aef1e817c5")