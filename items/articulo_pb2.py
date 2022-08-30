# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: articulo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='articulo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x61rticulo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x07\n\x05\x45mpty\"\xb6\x01\n\x04Item\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x0e\n\x06nombre\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scripcion\x18\x03 \x01(\t\x12\x0e\n\x06precio\x18\x04 \x01(\x01\x12\x10\n\x08\x63\x61ntidad\x18\x05 \x01(\x05\x12\x35\n\x11\x66\x65\x63ha_fabricacion\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x08\x63\x61tegory\x18\x07 \x01(\x0e\x32\r.ItemCategory\"2\n\x08ItemSale\x12\x11\n\tseller_id\x18\x01 \x01(\x05\x12\x13\n\x04item\x18\x02 \x01(\x0b\x32\x05.Item\"*\n\x06ItemId\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\"!\n\x05Items\x12\x18\n\x05items\x18\x01 \x03(\x0b\x32\t.ItemSale\"\"\n\x0fgetItemsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\xdc\x01\n\x10getItemsFiltered\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x1f\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.ItemCategory\x12\x0e\n\x06nombre\x18\x03 \x01(\t\x12\x11\n\tpreciomin\x18\x04 \x01(\x01\x12\x11\n\tpreciomax\x18\x05 \x01(\x01\x12/\n\x0b\x66\x65\x63ha_desde\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66\x65\x63ha_hasta\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x0e\x62uyItemRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\"#\n\x10ItemsCompraVenta\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"4\n\x18ItemsCompraVentaResponse\x12\x18\n\x05items\x18\x01 \x03(\x0b\x32\t.ItemSale\"1\n\x1b\x44ownloadProductImageRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\x05\"N\n\x08metadata\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\x12\x10\n\x08tipo_img\x18\x03 \x01(\t\x12\x0e\n\x06nombre\x18\x04 \x01(\t\"J\n\tDataChunk\x12\x0e\n\x04\x64\x61ta\x18\x01 \x01(\x0cH\x00\x12\"\n\rconfiguration\x18\x02 \x01(\x0b\x32\t.metadataH\x00\x42\t\n\x07request\"|\n\x15UploadProductResponse\x12:\n\rresult_status\x18\x01 \x01(\x0e\x32#.UploadProductResponse.ResultStatus\"\'\n\x0cResultStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01*b\n\x0cItemCategory\x12\x0e\n\nTECNOLOGIA\x10\x00\x12\n\n\x06LIBROS\x10\x01\x12\x0e\n\nVESTIMENTA\x10\x02\x12\r\n\tVEHICULOS\x10\x03\x12\x0c\n\x08\x44\x45PORTES\x10\x04\x12\t\n\x05HOGAR\x10\x05\x32\xee\x03\n\x0bItemService\x12\x1f\n\tNuevoItem\x12\t.ItemSale\x1a\x07.ItemId\x12 \n\nEditarItem\x12\t.ItemSale\x1a\x07.ItemId\x12\x1d\n\x07GetItem\x12\x07.ItemId\x1a\t.ItemSale\x12$\n\x08GetItems\x12\x10.getItemsRequest\x1a\x06.Items\x12-\n\x10GetItemsFiltered\x12\x11.getItemsFiltered\x1a\x06.Items\x12&\n\x0b\x43omprarItem\x12\x0f.buyItemRequest\x1a\x06.Empty\x12>\n\x0eItemsComprados\x12\x11.ItemsCompraVenta\x1a\x19.ItemsCompraVentaResponse\x12<\n\x0cItemsEnVenta\x12\x11.ItemsCompraVenta\x1a\x19.ItemsCompraVentaResponse\x12\x44\n\x14\x44ownloadProductImage\x12\x1c.DownloadProductImageRequest\x1a\n.DataChunk\"\x00\x30\x01\x12<\n\x12UploadProductImage\x12\n.DataChunk\x1a\x16.UploadProductResponse\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ITEMCATEGORY = _descriptor.EnumDescriptor(
  name='ItemCategory',
  full_name='ItemCategory',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TECNOLOGIA', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIBROS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VESTIMENTA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VEHICULOS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEPORTES', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOGAR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1111,
  serialized_end=1209,
)
_sym_db.RegisterEnumDescriptor(_ITEMCATEGORY)

ItemCategory = enum_type_wrapper.EnumTypeWrapper(_ITEMCATEGORY)
TECNOLOGIA = 0
LIBROS = 1
VESTIMENTA = 2
VEHICULOS = 3
DEPORTES = 4
HOGAR = 5


_UPLOADPRODUCTRESPONSE_RESULTSTATUS = _descriptor.EnumDescriptor(
  name='ResultStatus',
  full_name='UploadProductResponse.ResultStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1070,
  serialized_end=1109,
)
_sym_db.RegisterEnumDescriptor(_UPLOADPRODUCTRESPONSE_RESULTSTATUS)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=58,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='Item.item_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nombre', full_name='Item.nombre', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descripcion', full_name='Item.descripcion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='precio', full_name='Item.precio', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cantidad', full_name='Item.cantidad', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fecha_fabricacion', full_name='Item.fecha_fabricacion', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='Item.category', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=243,
)


_ITEMSALE = _descriptor.Descriptor(
  name='ItemSale',
  full_name='ItemSale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seller_id', full_name='ItemSale.seller_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item', full_name='ItemSale.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=295,
)


_ITEMID = _descriptor.Descriptor(
  name='ItemId',
  full_name='ItemId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='ItemId.item_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ItemId.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=339,
)


_ITEMS = _descriptor.Descriptor(
  name='Items',
  full_name='Items',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='Items.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=374,
)


_GETITEMSREQUEST = _descriptor.Descriptor(
  name='getItemsRequest',
  full_name='getItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='getItemsRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=410,
)


_GETITEMSFILTERED = _descriptor.Descriptor(
  name='getItemsFiltered',
  full_name='getItemsFiltered',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='getItemsFiltered.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='getItemsFiltered.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nombre', full_name='getItemsFiltered.nombre', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preciomin', full_name='getItemsFiltered.preciomin', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preciomax', full_name='getItemsFiltered.preciomax', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fecha_desde', full_name='getItemsFiltered.fecha_desde', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fecha_hasta', full_name='getItemsFiltered.fecha_hasta', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=633,
)


_BUYITEMREQUEST = _descriptor.Descriptor(
  name='buyItemRequest',
  full_name='buyItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='buyItemRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='buyItemRequest.item_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=685,
)


_ITEMSCOMPRAVENTA = _descriptor.Descriptor(
  name='ItemsCompraVenta',
  full_name='ItemsCompraVenta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ItemsCompraVenta.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=722,
)


_ITEMSCOMPRAVENTARESPONSE = _descriptor.Descriptor(
  name='ItemsCompraVentaResponse',
  full_name='ItemsCompraVentaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ItemsCompraVentaResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=776,
)


_DOWNLOADPRODUCTIMAGEREQUEST = _descriptor.Descriptor(
  name='DownloadProductImageRequest',
  full_name='DownloadProductImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='DownloadProductImageRequest.product_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=827,
)


_METADATA = _descriptor.Descriptor(
  name='metadata',
  full_name='metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='metadata.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='metadata.item_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tipo_img', full_name='metadata.tipo_img', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nombre', full_name='metadata.nombre', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=829,
  serialized_end=907,
)


_DATACHUNK = _descriptor.Descriptor(
  name='DataChunk',
  full_name='DataChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataChunk.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='DataChunk.configuration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='DataChunk.request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=909,
  serialized_end=983,
)


_UPLOADPRODUCTRESPONSE = _descriptor.Descriptor(
  name='UploadProductResponse',
  full_name='UploadProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_status', full_name='UploadProductResponse.result_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPLOADPRODUCTRESPONSE_RESULTSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=985,
  serialized_end=1109,
)

_ITEM.fields_by_name['fecha_fabricacion'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ITEM.fields_by_name['category'].enum_type = _ITEMCATEGORY
_ITEMSALE.fields_by_name['item'].message_type = _ITEM
_ITEMS.fields_by_name['items'].message_type = _ITEMSALE
_GETITEMSFILTERED.fields_by_name['category'].enum_type = _ITEMCATEGORY
_GETITEMSFILTERED.fields_by_name['fecha_desde'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETITEMSFILTERED.fields_by_name['fecha_hasta'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ITEMSCOMPRAVENTARESPONSE.fields_by_name['items'].message_type = _ITEMSALE
_DATACHUNK.fields_by_name['configuration'].message_type = _METADATA
_DATACHUNK.oneofs_by_name['request'].fields.append(
  _DATACHUNK.fields_by_name['data'])
_DATACHUNK.fields_by_name['data'].containing_oneof = _DATACHUNK.oneofs_by_name['request']
_DATACHUNK.oneofs_by_name['request'].fields.append(
  _DATACHUNK.fields_by_name['configuration'])
_DATACHUNK.fields_by_name['configuration'].containing_oneof = _DATACHUNK.oneofs_by_name['request']
_UPLOADPRODUCTRESPONSE.fields_by_name['result_status'].enum_type = _UPLOADPRODUCTRESPONSE_RESULTSTATUS
_UPLOADPRODUCTRESPONSE_RESULTSTATUS.containing_type = _UPLOADPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemSale'] = _ITEMSALE
DESCRIPTOR.message_types_by_name['ItemId'] = _ITEMID
DESCRIPTOR.message_types_by_name['Items'] = _ITEMS
DESCRIPTOR.message_types_by_name['getItemsRequest'] = _GETITEMSREQUEST
DESCRIPTOR.message_types_by_name['getItemsFiltered'] = _GETITEMSFILTERED
DESCRIPTOR.message_types_by_name['buyItemRequest'] = _BUYITEMREQUEST
DESCRIPTOR.message_types_by_name['ItemsCompraVenta'] = _ITEMSCOMPRAVENTA
DESCRIPTOR.message_types_by_name['ItemsCompraVentaResponse'] = _ITEMSCOMPRAVENTARESPONSE
DESCRIPTOR.message_types_by_name['DownloadProductImageRequest'] = _DOWNLOADPRODUCTIMAGEREQUEST
DESCRIPTOR.message_types_by_name['metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['DataChunk'] = _DATACHUNK
DESCRIPTOR.message_types_by_name['UploadProductResponse'] = _UPLOADPRODUCTRESPONSE
DESCRIPTOR.enum_types_by_name['ItemCategory'] = _ITEMCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  })
_sym_db.RegisterMessage(Item)

ItemSale = _reflection.GeneratedProtocolMessageType('ItemSale', (_message.Message,), {
  'DESCRIPTOR' : _ITEMSALE,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:ItemSale)
  })
_sym_db.RegisterMessage(ItemSale)

ItemId = _reflection.GeneratedProtocolMessageType('ItemId', (_message.Message,), {
  'DESCRIPTOR' : _ITEMID,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:ItemId)
  })
_sym_db.RegisterMessage(ItemId)

Items = _reflection.GeneratedProtocolMessageType('Items', (_message.Message,), {
  'DESCRIPTOR' : _ITEMS,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:Items)
  })
_sym_db.RegisterMessage(Items)

getItemsRequest = _reflection.GeneratedProtocolMessageType('getItemsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETITEMSREQUEST,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:getItemsRequest)
  })
_sym_db.RegisterMessage(getItemsRequest)

getItemsFiltered = _reflection.GeneratedProtocolMessageType('getItemsFiltered', (_message.Message,), {
  'DESCRIPTOR' : _GETITEMSFILTERED,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:getItemsFiltered)
  })
_sym_db.RegisterMessage(getItemsFiltered)

buyItemRequest = _reflection.GeneratedProtocolMessageType('buyItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUYITEMREQUEST,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:buyItemRequest)
  })
_sym_db.RegisterMessage(buyItemRequest)

ItemsCompraVenta = _reflection.GeneratedProtocolMessageType('ItemsCompraVenta', (_message.Message,), {
  'DESCRIPTOR' : _ITEMSCOMPRAVENTA,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:ItemsCompraVenta)
  })
_sym_db.RegisterMessage(ItemsCompraVenta)

ItemsCompraVentaResponse = _reflection.GeneratedProtocolMessageType('ItemsCompraVentaResponse', (_message.Message,), {
  'DESCRIPTOR' : _ITEMSCOMPRAVENTARESPONSE,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:ItemsCompraVentaResponse)
  })
_sym_db.RegisterMessage(ItemsCompraVentaResponse)

DownloadProductImageRequest = _reflection.GeneratedProtocolMessageType('DownloadProductImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADPRODUCTIMAGEREQUEST,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:DownloadProductImageRequest)
  })
_sym_db.RegisterMessage(DownloadProductImageRequest)

metadata = _reflection.GeneratedProtocolMessageType('metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:metadata)
  })
_sym_db.RegisterMessage(metadata)

DataChunk = _reflection.GeneratedProtocolMessageType('DataChunk', (_message.Message,), {
  'DESCRIPTOR' : _DATACHUNK,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:DataChunk)
  })
_sym_db.RegisterMessage(DataChunk)

UploadProductResponse = _reflection.GeneratedProtocolMessageType('UploadProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADPRODUCTRESPONSE,
  '__module__' : 'articulo_pb2'
  # @@protoc_insertion_point(class_scope:UploadProductResponse)
  })
_sym_db.RegisterMessage(UploadProductResponse)



_ITEMSERVICE = _descriptor.ServiceDescriptor(
  name='ItemService',
  full_name='ItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1212,
  serialized_end=1706,
  methods=[
  _descriptor.MethodDescriptor(
    name='NuevoItem',
    full_name='ItemService.NuevoItem',
    index=0,
    containing_service=None,
    input_type=_ITEMSALE,
    output_type=_ITEMID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditarItem',
    full_name='ItemService.EditarItem',
    index=1,
    containing_service=None,
    input_type=_ITEMSALE,
    output_type=_ITEMID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetItem',
    full_name='ItemService.GetItem',
    index=2,
    containing_service=None,
    input_type=_ITEMID,
    output_type=_ITEMSALE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetItems',
    full_name='ItemService.GetItems',
    index=3,
    containing_service=None,
    input_type=_GETITEMSREQUEST,
    output_type=_ITEMS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetItemsFiltered',
    full_name='ItemService.GetItemsFiltered',
    index=4,
    containing_service=None,
    input_type=_GETITEMSFILTERED,
    output_type=_ITEMS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ComprarItem',
    full_name='ItemService.ComprarItem',
    index=5,
    containing_service=None,
    input_type=_BUYITEMREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ItemsComprados',
    full_name='ItemService.ItemsComprados',
    index=6,
    containing_service=None,
    input_type=_ITEMSCOMPRAVENTA,
    output_type=_ITEMSCOMPRAVENTARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ItemsEnVenta',
    full_name='ItemService.ItemsEnVenta',
    index=7,
    containing_service=None,
    input_type=_ITEMSCOMPRAVENTA,
    output_type=_ITEMSCOMPRAVENTARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadProductImage',
    full_name='ItemService.DownloadProductImage',
    index=8,
    containing_service=None,
    input_type=_DOWNLOADPRODUCTIMAGEREQUEST,
    output_type=_DATACHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadProductImage',
    full_name='ItemService.UploadProductImage',
    index=9,
    containing_service=None,
    input_type=_DATACHUNK,
    output_type=_UPLOADPRODUCTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ITEMSERVICE)

DESCRIPTOR.services_by_name['ItemService'] = _ITEMSERVICE

# @@protoc_insertion_point(module_scope)