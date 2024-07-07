# MarketPlace gRPC Service

## Overview

<img src="/diagram.jpg" width="600">

The service is divided into two main components: the server and the client. The gRPC interface is defined in `market.proto`, with auto-generated Python code (`market_pb2.py` and `market_pb2_grpc.py`) facilitating the implementation of the service and client functionality.
### Features

- **Register Sellers**: Allows sellers to register in the marketplace.
- **Item Management**: Enables sellers to add, update, and delete items.
- **Search and Purchase**: Buyers can search for items and make purchases.
- **Wishlist**: Buyers can add items to a wishlist for future reference.
- **Rate Items**: Buyers can rate items they have purchased.

### Files Description

- `market.proto`: This file contains the Protobuf definitions for the service, including the RPC methods and message types used for requests and responses.
- `market_pb2.py` and `market_pb2_grpc.py`: These files are generated from `market.proto` using the protoc compiler. `market_pb2.py` contains message classes, and `market_pb2_grpc.py` includes server and client classes.
- `market_pb2.pyi`: This is a stub file providing type hints for `market_pb2.py`, improving code completion and type checking in IDEs.
- `market_server.py`: Implements the server-side logic for the marketplace service. It defines how each RPC call is handled.
- `buyer.py`: A client that demonstrates how to interact with the marketplace service, including registering sellers, adding items, and purchasing them.

### Prerequisites

- Python 3.6 or higher
- gRPC and gRPC tools for Python

You can install the necessary libraries using pip:

```bash
pip install grpcio grpcio-tools
```

### Generating gRPC Code

After any changes to `market.proto`, regenerate the python files using the following command::

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. market.proto
```

### Running the Server
Start the marketplace server by running:

```bash
python market_server.py
```

### Running the Client
To interact with the marketplace service, run the client script:

```bash
python buyer.py
```
