from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientNotificationRequest(_message.Message):
    __slots__ = ("item",)
    class Item(_message.Message):
        __slots__ = ("item_id", "price_per_unit", "product_name", "category", "description", "quantity", "ratings")
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        RATINGS_FIELD_NUMBER: _ClassVar[int]
        item_id: int
        price_per_unit: float
        product_name: str
        category: str
        description: str
        quantity: int
        ratings: float
        def __init__(self, item_id: _Optional[int] = ..., price_per_unit: _Optional[float] = ..., product_name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., quantity: _Optional[int] = ..., ratings: _Optional[float] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: ClientNotificationRequest.Item
    def __init__(self, item: _Optional[_Union[ClientNotificationRequest.Item, _Mapping]] = ...) -> None: ...

class ClientNotificationResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SellerNotificationRequest(_message.Message):
    __slots__ = ("item",)
    class Item(_message.Message):
        __slots__ = ("item_id", "price_per_unit", "product_name", "category", "description", "quantity", "ratings")
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        RATINGS_FIELD_NUMBER: _ClassVar[int]
        item_id: int
        price_per_unit: float
        product_name: str
        category: str
        description: str
        quantity: int
        ratings: float
        def __init__(self, item_id: _Optional[int] = ..., price_per_unit: _Optional[float] = ..., product_name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., quantity: _Optional[int] = ..., ratings: _Optional[float] = ...) -> None: ...
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: SellerNotificationRequest.Item
    def __init__(self, item: _Optional[_Union[SellerNotificationRequest.Item, _Mapping]] = ...) -> None: ...

class SellerNotificationResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RegisterSellerRequest(_message.Message):
    __slots__ = ("address", "uuid")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    address: str
    uuid: str
    def __init__(self, address: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class RegisterSellerResponse(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[RegisterSellerResponse.Status]
        FAILED: _ClassVar[RegisterSellerResponse.Status]
    SUCCESS: RegisterSellerResponse.Status
    FAILED: RegisterSellerResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RegisterSellerResponse.Status
    def __init__(self, status: _Optional[_Union[RegisterSellerResponse.Status, str]] = ...) -> None: ...

class SellItemRequest(_message.Message):
    __slots__ = ("product_name", "category", "quantity", "description", "seller_address", "price_per_unit", "seller_uuid")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    category: str
    quantity: int
    description: str
    seller_address: str
    price_per_unit: float
    seller_uuid: str
    def __init__(self, product_name: _Optional[str] = ..., category: _Optional[str] = ..., quantity: _Optional[int] = ..., description: _Optional[str] = ..., seller_address: _Optional[str] = ..., price_per_unit: _Optional[float] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class SellItemResponse(_message.Message):
    __slots__ = ("message", "item_id")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    item_id: int
    def __init__(self, message: _Optional[str] = ..., item_id: _Optional[int] = ...) -> None: ...

class UpdateItemRequest(_message.Message):
    __slots__ = ("item_id", "new_price", "new_quantity", "seller_address", "seller_uuid")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_PRICE_FIELD_NUMBER: _ClassVar[int]
    NEW_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    new_price: float
    new_quantity: int
    seller_address: str
    seller_uuid: str
    def __init__(self, item_id: _Optional[int] = ..., new_price: _Optional[float] = ..., new_quantity: _Optional[int] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class UpdateItemResponse(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[UpdateItemResponse.Status]
        FAILED: _ClassVar[UpdateItemResponse.Status]
    SUCCESS: UpdateItemResponse.Status
    FAILED: UpdateItemResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: UpdateItemResponse.Status
    def __init__(self, status: _Optional[_Union[UpdateItemResponse.Status, str]] = ...) -> None: ...

class DeleteItemRequest(_message.Message):
    __slots__ = ("item_id", "seller_address", "seller_uuid")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    seller_address: str
    seller_uuid: str
    def __init__(self, item_id: _Optional[int] = ..., seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class DeleteItemResponse(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[DeleteItemResponse.Status]
        FAILED: _ClassVar[DeleteItemResponse.Status]
    SUCCESS: DeleteItemResponse.Status
    FAILED: DeleteItemResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: DeleteItemResponse.Status
    def __init__(self, status: _Optional[_Union[DeleteItemResponse.Status, str]] = ...) -> None: ...

class DisplaySellerItemsRequest(_message.Message):
    __slots__ = ("seller_address", "seller_uuid")
    SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_UUID_FIELD_NUMBER: _ClassVar[int]
    seller_address: str
    seller_uuid: str
    def __init__(self, seller_address: _Optional[str] = ..., seller_uuid: _Optional[str] = ...) -> None: ...

class DisplaySellerItemsResponse(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("item_id", "price", "product_name", "category", "description", "quantity_remaining", "seller", "rating")
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_REMAINING_FIELD_NUMBER: _ClassVar[int]
        SELLER_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        item_id: int
        price: float
        product_name: str
        category: str
        description: str
        quantity_remaining: int
        seller: str
        rating: float
        def __init__(self, item_id: _Optional[int] = ..., price: _Optional[float] = ..., product_name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., quantity_remaining: _Optional[int] = ..., seller: _Optional[str] = ..., rating: _Optional[float] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DisplaySellerItemsResponse.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[DisplaySellerItemsResponse.Item, _Mapping]]] = ...) -> None: ...

class SearchItemRequest(_message.Message):
    __slots__ = ("item_name", "category")
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    item_name: str
    category: str
    def __init__(self, item_name: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...

class SearchItemResponse(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("item_id", "price", "product_name", "category", "description", "quantity_remaining", "rating", "seller_address")
        ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_REMAINING_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        SELLER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        item_id: int
        price: float
        product_name: str
        category: str
        description: str
        quantity_remaining: int
        rating: float
        seller_address: str
        def __init__(self, item_id: _Optional[int] = ..., price: _Optional[float] = ..., product_name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., quantity_remaining: _Optional[int] = ..., rating: _Optional[float] = ..., seller_address: _Optional[str] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SearchItemResponse.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[SearchItemResponse.Item, _Mapping]]] = ...) -> None: ...

class BuyItemRequest(_message.Message):
    __slots__ = ("item_id", "quantity", "buyer_address")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    quantity: int
    buyer_address: str
    def __init__(self, item_id: _Optional[int] = ..., quantity: _Optional[int] = ..., buyer_address: _Optional[str] = ...) -> None: ...

class BuyItemResponse(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[BuyItemResponse.Status]
        FAILED: _ClassVar[BuyItemResponse.Status]
    SUCCESS: BuyItemResponse.Status
    FAILED: BuyItemResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: BuyItemResponse.Status
    def __init__(self, status: _Optional[_Union[BuyItemResponse.Status, str]] = ...) -> None: ...

class AddToWishListRequest(_message.Message):
    __slots__ = ("item_id", "buyer_address")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    buyer_address: str
    def __init__(self, item_id: _Optional[int] = ..., buyer_address: _Optional[str] = ...) -> None: ...

class AddToWishListResponse(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[AddToWishListResponse.Status]
        FAILED: _ClassVar[AddToWishListResponse.Status]
    SUCCESS: AddToWishListResponse.Status
    FAILED: AddToWishListResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: AddToWishListResponse.Status
    def __init__(self, status: _Optional[_Union[AddToWishListResponse.Status, str]] = ...) -> None: ...

class RateItemRequest(_message.Message):
    __slots__ = ("item_id", "buyer_address", "rating")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BUYER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    buyer_address: str
    rating: int
    def __init__(self, item_id: _Optional[int] = ..., buyer_address: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...

class RateItemResponse(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[RateItemResponse.Status]
        FAILED: _ClassVar[RateItemResponse.Status]
    SUCCESS: RateItemResponse.Status
    FAILED: RateItemResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RateItemResponse.Status
    def __init__(self, status: _Optional[_Union[RateItemResponse.Status, str]] = ...) -> None: ...
