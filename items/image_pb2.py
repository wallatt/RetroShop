# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bimage.proto\"N\n\x12UploadImageRequest\x12\x1a\n\x04info\x18\x01 \x01(\x0b\x32\n.ImageInfoH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"+\n\tImageInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nimage_type\x18\x02 \x01(\t\"!\n\x13UploadImageResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1d\n\rRequestUpload\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x07\n\x05\x45mpty\"1\n\x1b\x44ownloadProductImageRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\x03\"M\n\tDataChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x0f\n\x07item_id\x18\x03 \x01(\x05\x12\x10\n\x08tipo_img\x18\x04 \x01(\t\"|\n\x15UploadProductResponse\x12:\n\rresult_status\x18\x01 \x01(\x0e\x32#.UploadProductResponse.ResultStatus\"\'\n\x0cResultStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x32\xbd\x01\n\x0cImageService\x12)\n\x0bUploadImage\x12\x0e.RequestUpload\x1a\x06.Empty\"\x00(\x01\x12\x44\n\x14\x44ownloadProductImage\x12\x1c.DownloadProductImageRequest\x1a\n.DataChunk\"\x00\x30\x01\x12<\n\x12UploadProductImage\x12\n.DataChunk\x1a\x16.UploadProductResponse\"\x00(\x01\x62\x06proto3'
)



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
  serialized_start=430,
  serialized_end=469,
)
_sym_db.RegisterEnumDescriptor(_UPLOADPRODUCTRESPONSE_RESULTSTATUS)


_UPLOADIMAGEREQUEST = _descriptor.Descriptor(
  name='UploadImageRequest',
  full_name='UploadImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='UploadImageRequest.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='UploadImageRequest.chunk_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
      name='data', full_name='UploadImageRequest.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=15,
  serialized_end=93,
)


_IMAGEINFO = _descriptor.Descriptor(
  name='ImageInfo',
  full_name='ImageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ImageInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_type', full_name='ImageInfo.image_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=95,
  serialized_end=138,
)


_UPLOADIMAGERESPONSE = _descriptor.Descriptor(
  name='UploadImageResponse',
  full_name='UploadImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UploadImageResponse.id', index=0,
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
  serialized_start=140,
  serialized_end=173,
)


_REQUESTUPLOAD = _descriptor.Descriptor(
  name='RequestUpload',
  full_name='RequestUpload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestUpload.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=175,
  serialized_end=204,
)


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
  serialized_start=206,
  serialized_end=213,
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
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=215,
  serialized_end=264,
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
      name='user_id', full_name='DataChunk.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='DataChunk.item_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tipo_img', full_name='DataChunk.tipo_img', index=3,
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
  serialized_start=266,
  serialized_end=343,
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
  serialized_start=345,
  serialized_end=469,
)

_UPLOADIMAGEREQUEST.fields_by_name['info'].message_type = _IMAGEINFO
_UPLOADIMAGEREQUEST.oneofs_by_name['data'].fields.append(
  _UPLOADIMAGEREQUEST.fields_by_name['info'])
_UPLOADIMAGEREQUEST.fields_by_name['info'].containing_oneof = _UPLOADIMAGEREQUEST.oneofs_by_name['data']
_UPLOADIMAGEREQUEST.oneofs_by_name['data'].fields.append(
  _UPLOADIMAGEREQUEST.fields_by_name['chunk_data'])
_UPLOADIMAGEREQUEST.fields_by_name['chunk_data'].containing_oneof = _UPLOADIMAGEREQUEST.oneofs_by_name['data']
_UPLOADPRODUCTRESPONSE.fields_by_name['result_status'].enum_type = _UPLOADPRODUCTRESPONSE_RESULTSTATUS
_UPLOADPRODUCTRESPONSE_RESULTSTATUS.containing_type = _UPLOADPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['UploadImageRequest'] = _UPLOADIMAGEREQUEST
DESCRIPTOR.message_types_by_name['ImageInfo'] = _IMAGEINFO
DESCRIPTOR.message_types_by_name['UploadImageResponse'] = _UPLOADIMAGERESPONSE
DESCRIPTOR.message_types_by_name['RequestUpload'] = _REQUESTUPLOAD
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['DownloadProductImageRequest'] = _DOWNLOADPRODUCTIMAGEREQUEST
DESCRIPTOR.message_types_by_name['DataChunk'] = _DATACHUNK
DESCRIPTOR.message_types_by_name['UploadProductResponse'] = _UPLOADPRODUCTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadImageRequest = _reflection.GeneratedProtocolMessageType('UploadImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADIMAGEREQUEST,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:UploadImageRequest)
  })
_sym_db.RegisterMessage(UploadImageRequest)

ImageInfo = _reflection.GeneratedProtocolMessageType('ImageInfo', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEINFO,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:ImageInfo)
  })
_sym_db.RegisterMessage(ImageInfo)

UploadImageResponse = _reflection.GeneratedProtocolMessageType('UploadImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADIMAGERESPONSE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:UploadImageResponse)
  })
_sym_db.RegisterMessage(UploadImageResponse)

RequestUpload = _reflection.GeneratedProtocolMessageType('RequestUpload', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTUPLOAD,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:RequestUpload)
  })
_sym_db.RegisterMessage(RequestUpload)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

DownloadProductImageRequest = _reflection.GeneratedProtocolMessageType('DownloadProductImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADPRODUCTIMAGEREQUEST,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:DownloadProductImageRequest)
  })
_sym_db.RegisterMessage(DownloadProductImageRequest)

DataChunk = _reflection.GeneratedProtocolMessageType('DataChunk', (_message.Message,), {
  'DESCRIPTOR' : _DATACHUNK,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:DataChunk)
  })
_sym_db.RegisterMessage(DataChunk)

UploadProductResponse = _reflection.GeneratedProtocolMessageType('UploadProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADPRODUCTRESPONSE,
  '__module__' : 'image_pb2'
  # @@protoc_insertion_point(class_scope:UploadProductResponse)
  })
_sym_db.RegisterMessage(UploadProductResponse)



_IMAGESERVICE = _descriptor.ServiceDescriptor(
  name='ImageService',
  full_name='ImageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=472,
  serialized_end=661,
  methods=[
  _descriptor.MethodDescriptor(
    name='UploadImage',
    full_name='ImageService.UploadImage',
    index=0,
    containing_service=None,
    input_type=_REQUESTUPLOAD,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DownloadProductImage',
    full_name='ImageService.DownloadProductImage',
    index=1,
    containing_service=None,
    input_type=_DOWNLOADPRODUCTIMAGEREQUEST,
    output_type=_DATACHUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadProductImage',
    full_name='ImageService.UploadProductImage',
    index=2,
    containing_service=None,
    input_type=_DATACHUNK,
    output_type=_UPLOADPRODUCTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESERVICE)

DESCRIPTOR.services_by_name['ImageService'] = _IMAGESERVICE

# @@protoc_insertion_point(module_scope)
