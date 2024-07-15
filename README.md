# MarketPlace gRPC Service

## Overview

<img src="/diagram.jpg" width="600">

The service is divided into two main components: the server and the client. The gRPC interface is defined in `market.proto`, with auto-generated Python code (`market_pb2.py` and `market_pb2_grpc.py`) facilitating the implementation of the service and client functionality.

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

#### 3. Run the Marketplace server by running:

```bash
python market_server.py
```

#### 4. Run the Client, to interact with the Marketplace:

```bash
python buyer.py
```
