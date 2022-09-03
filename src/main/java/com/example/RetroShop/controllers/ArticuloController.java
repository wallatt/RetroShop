package com.example.RetroShop.controllers;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.example.RetroShop.entities.ArticuloClient;
import com.example.RetroShop.helper.ViewRouteHelper;

import io.grpc.RetroShop.articulo.ItemSale;
import java.util.logging.Logger;



@RestController
public class ArticuloController {

    ArticuloClient cliente = new ArticuloClient("localhost", 50052);

    Logger logger = Logger.getLogger(ArticuloController.class.getName());


    @GetMapping("/item")
    public String login(){

        ItemSale item = cliente.getItem(9, 2);
        try{
            logger.info(item.getItem().toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        return item.toString();
    }

    // @GetMapping("/fotos")
    @ResponseBody
    @RequestMapping(value = "/fotos/{id_foto}", method = RequestMethod.GET, produces = MediaType.IMAGE_PNG_VALUE)
    public byte[] getfoto(@PathVariable String id_foto){
        logger.info("Se viene por aca el request");

        byte[] response = cliente.getImage(id_foto);

        return response;
    }

    @GetMapping("/nuevafoto")
    public String subirfoto(){
        try{
        cliente.subirImagen("C:/Users/Wallatt/Downloads/abc4.png", 2, 2);
        }catch(Exception e){
            logger.info("error cargando imagen "+e.getMessage());
        }
        return "hola";
    }

    @GetMapping("/nuevoarticulo")
    public String nuevoarticulo(){

        int idusuario = 2;

        String rutaFoto = "C:/Users/Wallatt/Downloads/abc5.png";
        String nombre = "Microondas";
        String descripcion = "Azul 5 años de uso";
        double precio = 650;
        int cantidad =2;
        try{
            cliente.nuevoArticulo(rutaFoto,idusuario,nombre,descripcion, precio, cantidad);
        }catch(Exception e){
            logger.info("error cargando imagen "+e.getMessage());
        }
        return "hola";
    }

    @GetMapping("/item/{id_item}")
    public ModelAndView getItems(@PathVariable("id_item") int id){
        ModelAndView mav = new ModelAndView(ViewRouteHelper.ARTICULOS);
        ItemSale item = cliente.getItem(id, 2);
        mav.addObject("Articulo", item);
        return mav;
        
    }


    
    
}
