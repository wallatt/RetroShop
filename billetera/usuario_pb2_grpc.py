# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import usuario_pb2 as usuario__pb2


class UsuarioStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NuevoUsuario = channel.unary_unary(
                '/usuario.Usuario/NuevoUsuario',
                request_serializer=usuario__pb2.CrearUsuarioRequest.SerializeToString,
                response_deserializer=usuario__pb2.UsuarioResponse.FromString,
                )
        self.UsuarioSesion = channel.unary_unary(
                '/usuario.Usuario/UsuarioSesion',
                request_serializer=usuario__pb2.IniciarSesionRequest.SerializeToString,
                response_deserializer=usuario__pb2.UserSesionResponse.FromString,
                )
        self.GetUsuario = channel.unary_unary(
                '/usuario.Usuario/GetUsuario',
                request_serializer=usuario__pb2.GetUsuarioRequest.SerializeToString,
                response_deserializer=usuario__pb2.GetPersonaResponse.FromString,
                )
        self.GetEstadoSesion = channel.unary_unary(
                '/usuario.Usuario/GetEstadoSesion',
                request_serializer=usuario__pb2.getSessionStatus.SerializeToString,
                response_deserializer=usuario__pb2.UserSesionResponse.FromString,
                )
        self.CloseSession = channel.unary_unary(
                '/usuario.Usuario/CloseSession',
                request_serializer=usuario__pb2.closeSessionRequest.SerializeToString,
                response_deserializer=usuario__pb2.empty.FromString,
                )


class UsuarioServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NuevoUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UsuarioSesion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEstadoSesion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsuarioServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NuevoUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.NuevoUsuario,
                    request_deserializer=usuario__pb2.CrearUsuarioRequest.FromString,
                    response_serializer=usuario__pb2.UsuarioResponse.SerializeToString,
            ),
            'UsuarioSesion': grpc.unary_unary_rpc_method_handler(
                    servicer.UsuarioSesion,
                    request_deserializer=usuario__pb2.IniciarSesionRequest.FromString,
                    response_serializer=usuario__pb2.UserSesionResponse.SerializeToString,
            ),
            'GetUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsuario,
                    request_deserializer=usuario__pb2.GetUsuarioRequest.FromString,
                    response_serializer=usuario__pb2.GetPersonaResponse.SerializeToString,
            ),
            'GetEstadoSesion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEstadoSesion,
                    request_deserializer=usuario__pb2.getSessionStatus.FromString,
                    response_serializer=usuario__pb2.UserSesionResponse.SerializeToString,
            ),
            'CloseSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseSession,
                    request_deserializer=usuario__pb2.closeSessionRequest.FromString,
                    response_serializer=usuario__pb2.empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'usuario.Usuario', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Usuario(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NuevoUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usuario.Usuario/NuevoUsuario',
            usuario__pb2.CrearUsuarioRequest.SerializeToString,
            usuario__pb2.UsuarioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UsuarioSesion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usuario.Usuario/UsuarioSesion',
            usuario__pb2.IniciarSesionRequest.SerializeToString,
            usuario__pb2.UserSesionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usuario.Usuario/GetUsuario',
            usuario__pb2.GetUsuarioRequest.SerializeToString,
            usuario__pb2.GetPersonaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEstadoSesion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usuario.Usuario/GetEstadoSesion',
            usuario__pb2.getSessionStatus.SerializeToString,
            usuario__pb2.UserSesionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/usuario.Usuario/CloseSession',
            usuario__pb2.closeSessionRequest.SerializeToString,
            usuario__pb2.empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)