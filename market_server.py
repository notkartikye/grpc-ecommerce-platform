import grpc
from concurrent import futures
import uuid

# Import generated proto modules
import market_pb2
import market_pb2_grpc


seller_database = {}
buyer_database = {}

# Define the MarketServicer class
class MarketService(market_pb2_grpc.MarketService):
    def __init__(self):
        self.item_id_counter = 1
        self.wishlist={}
        self.rating1={}
        self.tot_num={}
    def RegisterSeller(self, request, context):
        print(f"Seller join request from {request.address}")

        # Generate a unique UUID for the seller
        print(f"Generated UUID for {request.address}: {request.uuid}")

        if request.address in seller_database:
            print("Seller is already registered.")
            return market_pb2.RegisterSellerResponse(status=market_pb2.RegisterSellerResponse.Status.FAILED)

        # Register the seller with the generated UUID
        seller_database[request.address] = {
            'uuid': request.uuid,
            'items': []  # Placeholder for items the seller will sell
        }
        print("Seller registered successfully.")
        return market_pb2.RegisterSellerResponse(status=market_pb2.RegisterSellerResponse.Status.SUCCESS)
    

    def SellItem(self, request, context):
        print(f"Sell Item request from {request.seller_address}")

        # Check if the seller is registered
        if request.seller_address not in seller_database:
            print("Seller is not registered.")
            return market_pb2.SellItemResponse(status=market_pb2.SellItemResponse.Status.FAILED)

        # Validate input values
        if request.quantity <= 0:
            print("Invalid quantity. Quantity must be a positive integer.")
            return market_pb2.SellItemResponse(status=market_pb2.SellItemResponse.Status.FAILED)

        if request.price_per_unit <= 0:
            print("Invalid price per unit. Price per unit must be a positive float.")
            return market_pb2.SellItemResponse(status=market_pb2.SellItemResponse.Status.FAILED)

        if request.category not in ["ELECTRONICS", "FASHION", "OTHERS"]:
            print("Invalid category. Category must be one of ELECTRONICS, FASHION, or OTHERS.")
            return market_pb2.SellItemResponse(status=market_pb2.SellItemResponse.Status.FAILED)

        # Generate unique item ID
        item_id = self.item_id_counter
        self.item_id_counter += 1

        # Store item details
        item_details = {
            'item_id': item_id,
            'product_name': request.product_name,
            'category': request.category,
            'quantity': request.quantity,
            'description': request.description,
            'price_per_unit': request.price_per_unit,
            'ratings': 0.0  # Placeholder for buyer ratings
        }

        # Assign unique item ID to the product
        
        seller_database[request.seller_address]['items'].append(item_details)

        print("Item posted for sale successfully. Item ID:", item_id)
        return market_pb2.SellItemResponse(message = "SUCCESS", item_id=item_id)


    def UpdateItem(self, request, context):
        print(f"Update Item {request.item_id} request from {request.seller_address}")

        # Check if the seller is registered
        if request.seller_address not in seller_database:
            print("Seller is not registered.")
            return market_pb2.UpdateItemResponse(status=market_pb2.UpdateItemResponse.Status.FAILED)

        # Check if the item ID exists for the seller
        found = False
        for item in seller_database[request.seller_address]['items']:
            print(item)
            item_ids = item['item_id']
            if(item_ids == request.item_id):
                found = True
                break
        if found == False:
            print("Item does not exist for the seller.")
            return market_pb2.UpdateItemResponse(status=market_pb2.UpdateItemResponse.Status.FAILED)

        # Update item details
        item_to_up = None
        for item in seller_database[request.seller_address]['items']:
            print(item)
            item_ids = item['item_id']
            if(item_ids == request.item_id):
                item['price_per_unit']=request.new_price
                item['quantity']=request.new_quantity
                item_to_up = item
                break
        for buyer_address in self.wishlist:
            
            subset = self.wishlist[buyer_address]
            for item_id in subset:
                print("Item_id",item_id)
                if(item_id==item_to_up['item_id']):
                    
                    address = buyer_address
                    channel = grpc.insecure_channel(address)
                    stub = market_pb2_grpc.BuyerServiceStub(channel)

                    new_request = market_pb2.ClientNotificationRequest(item = item_to_up)
                    response = stub.BuyerNotification(new_request)
                    print("Notification sent successfully\n")    
        
        # self.wishlist[request.buyer_address].add(request.item_id)
        #notification_message = f"The item '{seller_database[request.seller_address]['items'][request.itemId]['product_name']}' (ID: {request.itemId}) has been updated. Check it out!"
        #self.notify_seller(notification_message, request, context.seller_address)
        
        return market_pb2.UpdateItemResponse(status=market_pb2.UpdateItemResponse.Status.SUCCESS)
    

    def DeleteItem(self, request, context):
        print(f"Delete Item {request.item_id} request from {request.seller_address}")

        # Check if the seller is registered
        if request.seller_address not in seller_database:
            print("Seller is not registered.")
            return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.Status.FAILED)

        # Check if the provided UUID matches the seller's UUID
        if seller_database[request.seller_address]['uuid'] != request.seller_uuid:
            print("Invalid seller UUID.")
            return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.Status.FAILED)

        # Check if the item ID is a valid positive integer
        if request.item_id <=0:
            print("Invalid item ID.")
            return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.Status.FAILED)

        # Check if the item ID exists for the seller
        found = False
        item_to_del=None
        for item in seller_database[request.seller_address]['items']:
            print(item)
            item_ids = item['item_id']
            if(item_ids == request.item_id):
                found = True
                item_to_del=item
                break
        seller_database[request.seller_address]['items'].remove(item_to_del)    
        if found == False:
        
            print("Item does not exist for the seller.")
            return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.Status.FAILED)

        # Delete item from the seller's items list
        # del seller_database[request.seller_address]['items'][request.item_id]

        print("Item deleted successfully.")
        return market_pb2.DeleteItemResponse(status=market_pb2.DeleteItemResponse.Status.SUCCESS)

    
    def DisplaySellerItems(self, request, context):
        print(f"Display Items request from {request.seller_address}")

    # Check if the seller is registered
        if request.seller_address not in seller_database:
            print("Seller is not registered.")
            return market_pb2.DisplaySellerItemsResponse()

        # Check if the provided UUID matches the seller's UUID (if provided)
        if request.seller_uuid:
            if seller_database[request.seller_address]['uuid'] != request.seller_uuid:
                print("Invalid seller UUID.")
                return market_pb2.DisplaySellerItemsResponse()

        # Fetch the seller's items
        seller_items = seller_database[request.seller_address]['items']

        # Prepare the response with seller's items details
        response = market_pb2.DisplaySellerItemsResponse()
        for items in seller_items:
             # Placeholder for buyer ratings
            item = response.items.add()
            item.item_id = items["item_id"]
            item.price = items['price_per_unit']
            item.product_name = items['product_name']
            item.category = items['category']
            item.seller=request.seller_address
            item.description = items['description']
            item.quantity_remaining = items['quantity']
            

            # Set rating if available, otherwise set it as 0
            
            item.rating = items['ratings']
            
        return response

    
    def SearchItem(self, request, context):
        print(f"Search request for Item name: {request.item_name or '<empty>'}, Category: {request.category}")

        # Initialize response
        response = market_pb2.SearchItemResponse()
        # print(seller_database.items())
        # Fetch all items matching the search criteria
        for seller_address in seller_database:
            seller_subset = seller_database[seller_address]
            for item_details in seller_subset['items']:
                # Check if item name and category match the search criteria
                if (request.item_name in item_details['product_name']) and (request.category == item_details['category']):
                    # Add item details to response
                    item = response.items.add()
                    item.item_id = item_details['item_id']
                    item.price = item_details['price_per_unit']
                    item.product_name = item_details['product_name']
                    item.category = item_details['category']
                    item.description = item_details['description']
                    item.quantity_remaining = item_details['quantity']

                    # Set rating if available, otherwise set it as 0
                    if 'rating' in item_details:
                        item.rating = item_details['rating']
                    else:
                        item.rating = 0

                    # Add seller details to item
                    item.seller_address = seller_address
                if(request.item_name in item_details['product_name']) and request.category=="ANY":
                    item = response.items.add()
                    item.item_id = item_details['item_id']
                    item.price = item_details['price_per_unit']
                    item.product_name = item_details['product_name']
                    item.category = item_details['category']
                    item.description = item_details['description']
                    item.quantity_remaining = item_details['quantity']

                    # Set rating if available, otherwise set it as 0
                    if 'rating' in item_details:
                        item.rating = item_details['rating']
                    else:
                        item.rating = 0

                    # Add seller details to item
                    item.seller_address = seller_address   
        return response

    
    def BuyItem(self, request, context):
        print(f"Buy request {request.quantity} of item {request.item_id}, from {request.buyer_address}")

    # Check if the item ID exists
        # seller_items = seller_database[request.seller_address]['items']
        for seller_address in seller_database:
            seller_database_sub = seller_database[seller_address]
            for items in seller_database_sub['items']:
                if(request.item_id == items['item_id']):
                    
           
                    if items['quantity'] >= request.quantity:
                        # Update item quantity
                        items['quantity'] -= request.quantity
                        print("Item purchased successfully.")
                        # Trigger notification to seller
                        #self.trigger_notification(seller_address, request, context.itemId)
                        address = seller_address
                        channel = grpc.insecure_channel(address)
                        stub = market_pb2_grpc.SellerServiceStub(channel)

                        new_request = market_pb2.SellerNotificationRequest(item = items)
                        response = stub.SellerNotification(new_request)
                        print("Notification sent successfully\n")
                        return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.Status.SUCCESS)
                    else:
                        print("Not enough stock available.")
                        return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.Status.FAILED)
        
        print("Invalid item ID.")
        return market_pb2.BuyItemResponse(status=market_pb2.BuyItemResponse.Status.FAILED)

    
    def AddToWishList(self, request, context):
        print(f"Wishlist request of item {request.item_id}, from {request.buyer_address}")
        # Your add to wishlist logic here
        for seller_address in seller_database:
            seller_database_sub = seller_database[seller_address]
            for items in seller_database_sub['items']:
                if(request.item_id == items['item_id']):
                    if request.buyer_address not in self.wishlist:
                        self.wishlist[request.buyer_address]=set()
                    self.wishlist[request.buyer_address].add(request.item_id)
                    return market_pb2.AddToWishListResponse(status=market_pb2.AddToWishListResponse.Status.SUCCESS)
        # For demonstration purposes, always return SUCCESS
        return market_pb2.AddToWishListResponse(status=market_pb2.AddToWishListResponse.Status.FAILED)

    
    def RateItem(self, request, context):
        print(f"{request.buyer_address} rated item {request.item_id} with {request.rating} stars.")
        # Your rate item logic here
        if(request.rating > 5 or request.rating < 1):
            
            return market_pb2.RateItemResponse(message = "FAILED: Invalid Rating")
        found1 = False
        for seller_address in seller_database:
            seller_database_sub = seller_database[seller_address]
            for items in seller_database_sub['items']:
                if(request.item_id == items['item_id']):
                    found1 = True
        if found1==False:
            return market_pb2.RateItemResponse(message="FAILED: Item not found")

        if request.item_id in self.rating1 and request.buyer_address in self.rating1[request.item_id]:
            return market_pb2.RateItemResponse(message="FAILED: Buyer already rated this item")
        
        if request.item_id not in self.rating1:
            self.rating1[request.item_id] = {}
        if request.item_id not in self.tot_num:
            self.tot_num[request.item_id]=0;
        self.rating1[request.item_id][request.buyer_address] = request.rating
        for seller_address in seller_database:
            for item in seller_database[seller_address]['items']:
                # print(item)
                item_ids = item['item_id']
                if(item_ids == request.item_id):
                    
                    item["ratings"]=((item["ratings"]*self.tot_num[request.item_id])+request.rating)/(self.tot_num[request.item_id]+1)
                    print(item["ratings"])
                    self.tot_num[request.item_id]+=1
        #self.item_registry[request.item_id].average_rating = ((self.item_registry[request.item_id].average_rating * self.tot_num) + request.rating)/(self.tot_num+1)
        #self.tot_num += 1
        return market_pb2.RateItemResponse(status=market_pb2.RateItemResponse.Status.SUCCESS)
        #return market_pb2.RateItemResponse(message="SUCCESS")
        # For demonstration purposes, always return SUCCESS
        #return market_pb2.RateItemResponse(status=market_pb2.RateItemResponse.Status.SUCCESS)
    # Implement the remaining RPC methods similarly

# Function to serve the Market gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_MarketServiceServicer_to_server(MarketService(), server)
    server.add_insecure_port('[::]:50051')  # Use the desired port for your market server
    server.start()
    print("Market server started. Listening on port 50051")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
