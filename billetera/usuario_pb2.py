# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: usuario.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='usuario.proto',
  package='usuario',
  syntax='proto3',
  serialized_options=b'\n\031io.grpc.RetroShop.usuarioB\014usuarioProtoP\001\242\002\003USP',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rusuario.proto\x12\x07usuario\"R\n\x07Persona\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06nombre\x18\x02 \x01(\t\x12\x10\n\x08\x61pellido\x18\x03 \x01(\t\x12\x0b\n\x03\x64ni\x18\x04 \x01(\x05\x12\x0c\n\x04mail\x18\x05 \x01(\t\"1\n\x06\x43uenta\x12\x0f\n\x07usuario\x18\x01 \x01(\t\x12\x16\n\x0ehashedPassword\x18\x02 \x01(\t\"Y\n\x13\x43rearUsuarioRequest\x12!\n\x07persona\x18\x01 \x01(\x0b\x32\x10.usuario.Persona\x12\x1f\n\x06\x63uenta\x18\x02 \x01(\x0b\x32\x0f.usuario.Cuenta\"\x1d\n\x0fUsuarioResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"7\n\x14IniciarSesionRequest\x12\x1f\n\x06\x63uenta\x18\x01 \x01(\x0b\x32\x0f.usuario.Cuenta\"\x1f\n\x11GetUsuarioRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"X\n\x12GetPersonaResponse\x12!\n\x07persona\x18\x01 \x01(\x0b\x32\x10.usuario.Persona\x12\x1f\n\x06\x63uenta\x18\x02 \x01(\x0b\x32\x0f.usuario.Cuenta\"K\n\nUserSesion\x12\x11\n\tid_sesion\x18\x01 \x01(\x05\x12\x12\n\nid_persona\x18\x02 \x01(\x05\x12\x16\n\x0eisActiveSesion\x18\x03 \x01(\x08\"=\n\x12UserSesionResponse\x12\'\n\nuserSesion\x18\x01 \x01(\x0b\x32\x13.usuario.UserSesion\"9\n\x10getSessionStatus\x12\x11\n\tid_sesion\x18\x01 \x01(\x05\x12\x12\n\nid_persona\x18\x02 \x01(\x05\"<\n\x13\x63loseSessionRequest\x12\x11\n\tid_sesion\x18\x01 \x01(\x05\x12\x12\n\nid_persona\x18\x02 \x01(\x05\"\x07\n\x05\x65mpty2\xee\x02\n\x07Usuario\x12\x46\n\x0cNuevoUsuario\x12\x1c.usuario.CrearUsuarioRequest\x1a\x18.usuario.UsuarioResponse\x12K\n\rUsuarioSesion\x12\x1d.usuario.IniciarSesionRequest\x1a\x1b.usuario.UserSesionResponse\x12\x45\n\nGetUsuario\x12\x1a.usuario.GetUsuarioRequest\x1a\x1b.usuario.GetPersonaResponse\x12I\n\x0fGetEstadoSesion\x12\x19.usuario.getSessionStatus\x1a\x1b.usuario.UserSesionResponse\x12<\n\x0c\x43loseSession\x12\x1c.usuario.closeSessionRequest\x1a\x0e.usuario.emptyB1\n\x19io.grpc.RetroShop.usuarioB\x0cusuarioProtoP\x01\xa2\x02\x03USPb\x06proto3'
)




_PERSONA = _descriptor.Descriptor(
  name='Persona',
  full_name='usuario.Persona',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='usuario.Persona.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nombre', full_name='usuario.Persona.nombre', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='apellido', full_name='usuario.Persona.apellido', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dni', full_name='usuario.Persona.dni', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mail', full_name='usuario.Persona.mail', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=108,
)


_CUENTA = _descriptor.Descriptor(
  name='Cuenta',
  full_name='usuario.Cuenta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='usuario', full_name='usuario.Cuenta.usuario', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hashedPassword', full_name='usuario.Cuenta.hashedPassword', index=1,
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
  serialized_start=110,
  serialized_end=159,
)


_CREARUSUARIOREQUEST = _descriptor.Descriptor(
  name='CrearUsuarioRequest',
  full_name='usuario.CrearUsuarioRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persona', full_name='usuario.CrearUsuarioRequest.persona', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cuenta', full_name='usuario.CrearUsuarioRequest.cuenta', index=1,
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
  serialized_start=161,
  serialized_end=250,
)


_USUARIORESPONSE = _descriptor.Descriptor(
  name='UsuarioResponse',
  full_name='usuario.UsuarioResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='usuario.UsuarioResponse.id', index=0,
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
  serialized_start=252,
  serialized_end=281,
)


_INICIARSESIONREQUEST = _descriptor.Descriptor(
  name='IniciarSesionRequest',
  full_name='usuario.IniciarSesionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cuenta', full_name='usuario.IniciarSesionRequest.cuenta', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=283,
  serialized_end=338,
)


_GETUSUARIOREQUEST = _descriptor.Descriptor(
  name='GetUsuarioRequest',
  full_name='usuario.GetUsuarioRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='usuario.GetUsuarioRequest.id', index=0,
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
  serialized_start=340,
  serialized_end=371,
)


_GETPERSONARESPONSE = _descriptor.Descriptor(
  name='GetPersonaResponse',
  full_name='usuario.GetPersonaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persona', full_name='usuario.GetPersonaResponse.persona', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cuenta', full_name='usuario.GetPersonaResponse.cuenta', index=1,
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
  serialized_start=373,
  serialized_end=461,
)


_USERSESION = _descriptor.Descriptor(
  name='UserSesion',
  full_name='usuario.UserSesion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_sesion', full_name='usuario.UserSesion.id_sesion', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id_persona', full_name='usuario.UserSesion.id_persona', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isActiveSesion', full_name='usuario.UserSesion.isActiveSesion', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=463,
  serialized_end=538,
)


_USERSESIONRESPONSE = _descriptor.Descriptor(
  name='UserSesionResponse',
  full_name='usuario.UserSesionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userSesion', full_name='usuario.UserSesionResponse.userSesion', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=540,
  serialized_end=601,
)


_GETSESSIONSTATUS = _descriptor.Descriptor(
  name='getSessionStatus',
  full_name='usuario.getSessionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_sesion', full_name='usuario.getSessionStatus.id_sesion', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id_persona', full_name='usuario.getSessionStatus.id_persona', index=1,
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
  serialized_start=603,
  serialized_end=660,
)


_CLOSESESSIONREQUEST = _descriptor.Descriptor(
  name='closeSessionRequest',
  full_name='usuario.closeSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_sesion', full_name='usuario.closeSessionRequest.id_sesion', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id_persona', full_name='usuario.closeSessionRequest.id_persona', index=1,
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
  serialized_start=662,
  serialized_end=722,
)


_EMPTY = _descriptor.Descriptor(
  name='empty',
  full_name='usuario.empty',
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
  serialized_start=724,
  serialized_end=731,
)

_CREARUSUARIOREQUEST.fields_by_name['persona'].message_type = _PERSONA
_CREARUSUARIOREQUEST.fields_by_name['cuenta'].message_type = _CUENTA
_INICIARSESIONREQUEST.fields_by_name['cuenta'].message_type = _CUENTA
_GETPERSONARESPONSE.fields_by_name['persona'].message_type = _PERSONA
_GETPERSONARESPONSE.fields_by_name['cuenta'].message_type = _CUENTA
_USERSESIONRESPONSE.fields_by_name['userSesion'].message_type = _USERSESION
DESCRIPTOR.message_types_by_name['Persona'] = _PERSONA
DESCRIPTOR.message_types_by_name['Cuenta'] = _CUENTA
DESCRIPTOR.message_types_by_name['CrearUsuarioRequest'] = _CREARUSUARIOREQUEST
DESCRIPTOR.message_types_by_name['UsuarioResponse'] = _USUARIORESPONSE
DESCRIPTOR.message_types_by_name['IniciarSesionRequest'] = _INICIARSESIONREQUEST
DESCRIPTOR.message_types_by_name['GetUsuarioRequest'] = _GETUSUARIOREQUEST
DESCRIPTOR.message_types_by_name['GetPersonaResponse'] = _GETPERSONARESPONSE
DESCRIPTOR.message_types_by_name['UserSesion'] = _USERSESION
DESCRIPTOR.message_types_by_name['UserSesionResponse'] = _USERSESIONRESPONSE
DESCRIPTOR.message_types_by_name['getSessionStatus'] = _GETSESSIONSTATUS
DESCRIPTOR.message_types_by_name['closeSessionRequest'] = _CLOSESESSIONREQUEST
DESCRIPTOR.message_types_by_name['empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Persona = _reflection.GeneratedProtocolMessageType('Persona', (_message.Message,), {
  'DESCRIPTOR' : _PERSONA,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.Persona)
  })
_sym_db.RegisterMessage(Persona)

Cuenta = _reflection.GeneratedProtocolMessageType('Cuenta', (_message.Message,), {
  'DESCRIPTOR' : _CUENTA,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.Cuenta)
  })
_sym_db.RegisterMessage(Cuenta)

CrearUsuarioRequest = _reflection.GeneratedProtocolMessageType('CrearUsuarioRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREARUSUARIOREQUEST,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.CrearUsuarioRequest)
  })
_sym_db.RegisterMessage(CrearUsuarioRequest)

UsuarioResponse = _reflection.GeneratedProtocolMessageType('UsuarioResponse', (_message.Message,), {
  'DESCRIPTOR' : _USUARIORESPONSE,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.UsuarioResponse)
  })
_sym_db.RegisterMessage(UsuarioResponse)

IniciarSesionRequest = _reflection.GeneratedProtocolMessageType('IniciarSesionRequest', (_message.Message,), {
  'DESCRIPTOR' : _INICIARSESIONREQUEST,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.IniciarSesionRequest)
  })
_sym_db.RegisterMessage(IniciarSesionRequest)

GetUsuarioRequest = _reflection.GeneratedProtocolMessageType('GetUsuarioRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSUARIOREQUEST,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.GetUsuarioRequest)
  })
_sym_db.RegisterMessage(GetUsuarioRequest)

GetPersonaResponse = _reflection.GeneratedProtocolMessageType('GetPersonaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSONARESPONSE,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.GetPersonaResponse)
  })
_sym_db.RegisterMessage(GetPersonaResponse)

UserSesion = _reflection.GeneratedProtocolMessageType('UserSesion', (_message.Message,), {
  'DESCRIPTOR' : _USERSESION,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.UserSesion)
  })
_sym_db.RegisterMessage(UserSesion)

UserSesionResponse = _reflection.GeneratedProtocolMessageType('UserSesionResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERSESIONRESPONSE,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.UserSesionResponse)
  })
_sym_db.RegisterMessage(UserSesionResponse)

getSessionStatus = _reflection.GeneratedProtocolMessageType('getSessionStatus', (_message.Message,), {
  'DESCRIPTOR' : _GETSESSIONSTATUS,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.getSessionStatus)
  })
_sym_db.RegisterMessage(getSessionStatus)

closeSessionRequest = _reflection.GeneratedProtocolMessageType('closeSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSESESSIONREQUEST,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.closeSessionRequest)
  })
_sym_db.RegisterMessage(closeSessionRequest)

empty = _reflection.GeneratedProtocolMessageType('empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'usuario_pb2'
  # @@protoc_insertion_point(class_scope:usuario.empty)
  })
_sym_db.RegisterMessage(empty)


DESCRIPTOR._options = None

_USUARIO = _descriptor.ServiceDescriptor(
  name='Usuario',
  full_name='usuario.Usuario',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=734,
  serialized_end=1100,
  methods=[
  _descriptor.MethodDescriptor(
    name='NuevoUsuario',
    full_name='usuario.Usuario.NuevoUsuario',
    index=0,
    containing_service=None,
    input_type=_CREARUSUARIOREQUEST,
    output_type=_USUARIORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UsuarioSesion',
    full_name='usuario.Usuario.UsuarioSesion',
    index=1,
    containing_service=None,
    input_type=_INICIARSESIONREQUEST,
    output_type=_USERSESIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUsuario',
    full_name='usuario.Usuario.GetUsuario',
    index=2,
    containing_service=None,
    input_type=_GETUSUARIOREQUEST,
    output_type=_GETPERSONARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEstadoSesion',
    full_name='usuario.Usuario.GetEstadoSesion',
    index=3,
    containing_service=None,
    input_type=_GETSESSIONSTATUS,
    output_type=_USERSESIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseSession',
    full_name='usuario.Usuario.CloseSession',
    index=4,
    containing_service=None,
    input_type=_CLOSESESSIONREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USUARIO)

DESCRIPTOR.services_by_name['Usuario'] = _USUARIO

# @@protoc_insertion_point(module_scope)
