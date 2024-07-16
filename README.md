# Marketplace Service using gRPC
This is a gRPC-based marketplace service for distributed systems that connects buyers and sellers through a central market server. The service is divided into two main components— the server and the client. The gRPC interface is defined in `market.proto`, with auto-generated Python code (`market_pb2.py` and `market_pb2_grpc.py`) facilitating the implementation of the service and client functionality.


<img src="/diagram.jpg" width="550">


## Features

- **Register Sellers**: Allows sellers to register in the marketplace.
- **Item Management**: Enables sellers to add, update, and delete items.
- **Search and Purchase**: Buyers can search for items and make purchases.
- **Wishlist**: Buyers can add items to a wishlist for future reference.
- **Rate Items**: Buyers can rate items they have purchased.


## Getting Started

#### 1. Install the necessary gRPC libraries using pip:

```bash
pip install grpcio grpcio-tools
```

#### 2. Generate the gRPC code by running:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. market.proto
```

> *Note: The gRPC code needs to be generated after any changes are made to `market.proto`*

#### 3. Run the marketplace server by running:

```bash
python market_server.py
```

#### 4. Run the client, to interact with the marketplace:

```bash
python buyer.py
```

```bash
python seller.py
```
