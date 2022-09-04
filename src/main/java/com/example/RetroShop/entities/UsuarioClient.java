package com.example.RetroShop.entities;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;



import io.grpc.RetroShop.usuario.*;
import io.grpc.RetroShop.usuario.UsuarioGrpc.*;
// import io.grpc.RetroShop.usuario.UsuarioGrpc.*;

/**
 * A simple client that requests a greeting from the {@link UsuarioServer}.
 */

public class UsuarioClient {

    private static final Logger logger = Logger.getLogger(UsuarioClient.class.getName());


    private final ManagedChannel channel;
    private final UsuarioBlockingStub blockingStub;

    public UsuarioClient(String host, int port){
        channel = ManagedChannelBuilder.forAddress(host,port).usePlaintext().build();
        blockingStub = UsuarioGrpc.newBlockingStub(channel);
    }

    public void shutdown() throws InterruptedException{
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }


    public Persona getUsuario(int id_usuario){
        GetUsuarioRequest request = GetUsuarioRequest.newBuilder().setId(id_usuario).build();
        GetPersonaResponse response = GetPersonaResponse.getDefaultInstance();
        try{
            logger.info("intentando obtener usuario "+ id_usuario);
            response = blockingStub.getUsuario(request);
        }
        catch (StatusRuntimeException e) {
            return null;
        }
        return response.getPersona();
    }
    
    public boolean esSesionActiva(int id_usuario,int id_sesion){
        getSessionStatus request = getSessionStatus.newBuilder().setIdPersona(id_usuario).setIdSesion(id_sesion).build();
        UserSesionResponse response;
        try{
            logger.info("intentando obtener usuario "+ id_usuario);
            response = blockingStub.getEstadoSesion(request);
        }
        catch (StatusRuntimeException e) {
            return false;
        }
        return response.getUserSesion().getIsActiveSesion();
    }
    
    public int crearUsuario(int id, String nombre, String apellido, int dni, String mail, String usuario, String password){
        Persona persona = Persona.newBuilder().setId(id).
        setNombre(nombre).
        setApellido(apellido).
        setDni(dni).
        setMail(mail).        
        build();
        logger.info("creando cuenta y usuario"+usuario+ "   "+ password);
        Cuenta cuenta = Cuenta.newBuilder().setUsuario(usuario).setHashedPassword(password).build();
        CrearUsuarioRequest request = CrearUsuarioRequest.newBuilder().setPersona(persona).setCuenta(cuenta).build();
        logger.info("creado cuenta y usuario");
        UsuarioResponse response;
        try{
            logger.info("intentando generar nuevo usuario ");
            response = blockingStub.nuevoUsuario(request);
        }
        catch (StatusRuntimeException e) {
            return 0;
        }
        return response.getId();
    }
    
    public UserSesion iniciarSesion(String usuario, String password){
        Cuenta cuenta = Cuenta.newBuilder().setUsuario(usuario).setHashedPassword(password).build();
        IniciarSesionRequest request = IniciarSesionRequest.newBuilder().setCuenta(cuenta).build();
        UserSesionResponse response;
        try{
            logger.info("intentando generar nuevo usuario ");
            response = blockingStub.usuarioSesion(request);
        }
        catch (StatusRuntimeException e) {
            return null;
        }
        return response.getUserSesion();
    }
    
    public void cerrarSesion(int id_usuario, int id_sesion){
        closeSessionRequest request = closeSessionRequest.newBuilder().
                                    setIdPersona(id_usuario).
                                    setIdSesion(id_sesion).build();
        try{
            logger.info("intentando generar nuevo usuario ");
            blockingStub.closeSession(request);
        }
        catch (StatusRuntimeException e) {
        }
    }







    
}
