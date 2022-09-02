package com.example.RetroShop.controllers;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.RetroShop.entities.ArticuloClient;

import io.grpc.RetroShop.articulo.ItemSale;
import java.util.logging.Logger;



@RestController
public class ArticuloController {
    ArticuloClient cliente = new ArticuloClient("localhost", 50052);

    Logger logger = Logger.getLogger(ArticuloController.class.getName());


    @GetMapping("/item")
    public String login(){

        ItemSale item = cliente.getItem(1, 2);
        try{
            logger.info(item.getItem().toString());
        }catch(Exception e){
            logger.info(" "+e);
        }
        return item.toString();
    }

    // @GetMapping("/fotos")
    @ResponseBody
    @RequestMapping(value = "/fotos", method = RequestMethod.GET, produces = MediaType.IMAGE_PNG_VALUE)
    public byte[] getfoto(){
        logger.info("Se viene por aca el request");

        byte[] response = cliente.getImage("abc1.png");

        // try{
        //     logger.info(item.getItem().toString());
        // }catch(Exception e){
        //     logger.info(" "+e);
        // }
        // return item.toString();
        return response;
    }

    
    
}
