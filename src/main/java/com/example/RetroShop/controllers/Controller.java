package com.example.RetroShop.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.RetroShop.entities.HelloWorldClient;
import com.example.RetroShop.entities.UsuarioClient;

import io.grpc.RetroShop.usuario.Persona;
import io.grpc.RetroShop.usuario.UserSesion;

import java.util.logging.Logger;


@RestController
public class Controller {

    UsuarioClient hello = new UsuarioClient("localhost", 50051);

    Logger logger = Logger.getLogger(Controller.class.getName());

    @GetMapping("/nuevoUsuario")
    public String holamundo(){

        int idusuario = hello.crearUsuario(2,"Horacio", "Pagani", 45678, "hp@gmail.com", "Gallardo", "abc");

        logger.info("id de usuario devuelto: " + idusuario);
        Persona resultado = hello.getUsuario(idusuario);


        try{

            logger.info(resultado.toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        return resultado.toString();
    }
    
    @GetMapping("/login")
    public String login(){

        UserSesion sesion = hello.iniciarSesion("Gallardo", "abc");

        // logger.info("id de usuario devuelto: " + sesion);
        //Persona resultado = hello.getUsuario(idusuario);


        try{

            logger.info(sesion.toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        return sesion.toString();
    }


    
}
