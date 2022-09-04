package com.example.RetroShop.controllers;

import org.apache.catalina.authenticator.SavedRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.view.RedirectView;

import com.example.RetroShop.entities.UsuarioClient;
import com.example.RetroShop.helper.ViewRouteHelper;
import com.example.RetroShop.models.CuentaModel;
import com.example.RetroShop.models.Usuario;

import io.grpc.RetroShop.usuario.Persona;
import io.grpc.RetroShop.usuario.UserSesion;
import java.util.logging.Logger;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;


@RestController
public class UsuarioController {

    UsuarioClient cliente = new UsuarioClient("localhost", 50051);

    Logger logger = Logger.getLogger(UsuarioController.class.getName());

    @GetMapping("/nuevoUsuario")
    public String register(){

        int idusuario = cliente.crearUsuario(2,"Horacio", "Pagani", 45678, "hp@gmail.com", "Gallardo", "abc");

        logger.info("id de usuario devuelto: " + idusuario);
        Persona resultado = cliente.getUsuario(idusuario);
        try{
            logger.info(resultado.toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        return resultado.toString();
    }

 
  

    @GetMapping("/usuario/{id_usuario}")
    public String login(@PathVariable int id_usuario){

        Persona persona = cliente.getUsuario(id_usuario);
        try{
            logger.info(persona.toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        return persona.toString();
    }

    @GetMapping("/ingresar")
    public ModelAndView ingreso(){
        ModelAndView mav = new ModelAndView(ViewRouteHelper.INGRESO);
        mav.addObject("estado", "empty");
        mav.addObject("usuario", new Usuario());
        mav.addObject("cuenta", new CuentaModel());
        return mav;
    }

    @PostMapping("/user/create")
	public ModelAndView create(@ModelAttribute("user") Usuario usuario) throws Exception {
        ModelAndView mav = new ModelAndView(ViewRouteHelper.INGRESO);

        int id = cliente.crearUsuario(0, 
        usuario.getNombre(),
        usuario.getApellido(),
        usuario.getDni(),
        usuario.getMail(),
        usuario.getUsuario(),
        usuario.getPassword());

        if(id>=1){
        mav.addObject("estado", "success");
        }else{
        mav.addObject("estado", "fail");
        }
        return mav;
    
	}

    @GetMapping("/")
    public RedirectView indexview(){
        return new RedirectView("/ingresar");
    }

    @PostMapping("/login")
    public RedirectView login(@ModelAttribute("cuenta") CuentaModel cuenta, HttpServletResponse response){
        ModelAndView mav;
        logger.info("cuenta :"+ cuenta.getNombreUsuario());
        logger.info("contrasena :"+ cuenta.getPassword());
        UserSesion sesion = cliente.iniciarSesion(cuenta.getNombreUsuario(), cuenta.getPassword());
        try{
            logger.info(sesion.toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        if(sesion == null || sesion.getIdSesion() == 0){
            mav = new ModelAndView(ViewRouteHelper.INGRESO);
            mav.addObject("estado", "fail");
            return new RedirectView("/ingresar");
        }
        int iduser = sesion.getIdPersona();
        Persona persona = cliente.getUsuario(iduser);
        mav = new ModelAndView();
        mav.addObject("usuario", persona);
        String nombre = persona.getNombre();
        String apellido = persona.getApellido();
        int id_sesion = sesion.getIdSesion();
        int id_usuario = sesion.getIdSesion();
        logger.info("nombre: "+nombre);
        logger.info("apellido: "+apellido);
        logger.info("id_sesion: "+id_sesion);
        logger.info("id_usuario: "+id_usuario);
        Cookie cookie = new Cookie("nombre", nombre);
        Cookie cookie1 = new Cookie("apellido", apellido);
        Cookie cookie2 = new Cookie("id_sesion", ""+id_sesion);
        Cookie cookie3 = new Cookie("id_usuario", ""+id_usuario);
        response.addCookie(cookie);
        response.addCookie(cookie1);
        response.addCookie(cookie2);
        response.addCookie(cookie3);


		return new RedirectView("/items");

    }
    

    
}
    
        

