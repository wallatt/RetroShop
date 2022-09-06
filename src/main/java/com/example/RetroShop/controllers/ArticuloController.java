package com.example.RetroShop.controllers;

import org.springframework.http.MediaType;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.view.RedirectView;

import com.example.RetroShop.entities.ArticuloClient;
import com.example.RetroShop.entities.BilleteraClient;
import com.example.RetroShop.helper.ViewRouteHelper;
import com.example.RetroShop.models.Articulo;
import com.example.RetroShop.models.Compra;
import com.example.RetroShop.models.Filtro;
import com.example.RetroShop.models.ImagenWrapper;
import com.example.RetroShop.models.Saldo;
import com.example.RetroShop.models.Venta;

import io.grpc.RetroShop.articulo.ItemCategory;
import io.grpc.RetroShop.articulo.ItemSale;
import io.grpc.RetroShop.articulo.Items;
import io.grpc.RetroShop.articulo.ItemsCompraVentaResponse;
import com.google.protobuf.Timestamp;


import java.io.InputStream;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.logging.Logger;




@RestController
public class ArticuloController {

    ArticuloClient cliente = new ArticuloClient("localhost", 50052);
    BilleteraClient billetera = new BilleteraClient("localhost", 50053);

    Logger logger = Logger.getLogger(ArticuloController.class.getName());

    @ResponseBody
    @RequestMapping(value = "/fotos/{id_foto}", method = RequestMethod.GET, produces = MediaType.IMAGE_PNG_VALUE)
    public byte[] getfoto(@PathVariable String id_foto){
        logger.info("Resolviendo imagen request");

        byte[] response = cliente.getImage(id_foto);

        return response;
    }


    @GetMapping("/item/{id_item}")
    public ModelAndView getItem(@PathVariable("id_item") int id){
        ModelAndView mav = new ModelAndView(ViewRouteHelper.ARTICULO);
        ItemSale item = cliente.getItem(id, 2);

        Compra compra = new Compra();
 
        mav.addObject("compra", compra);
        mav.addObject("Articulo", item);
        return mav;
    }
    

    @GetMapping("/items")
    public ModelAndView getItems(@CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                                @RequestParam(required = false) String nombre,
                                @RequestParam(required = false) String categoria,
                                @RequestParam(required = false) String precioMin,
                                @RequestParam(required = false) String precioMax,
                                @RequestParam(required = false) String fechaMin,
                                @RequestParam(required = false) String fechaMax
    ){

        Filtro filtro = new Filtro(nombre, categoria, precioMin, precioMax, fechaMin,fechaMax);
        ModelAndView mav = new ModelAndView(ViewRouteHelper.ARTICULOS);

        int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }

        Items items  = cliente.getItems(user_id);
        
        if(filtro.isConParametros()){
            items = cliente.getFiltrados(filtro, user_id);
        }else{
            items = cliente.getItems(user_id);
        }
        if(items == null){
            items = cliente.getItems(user_id);
        }
        
        
        List<Articulo> articulos = new ArrayList<Articulo>();
        if(items != null){

            for(ItemSale i:items.getItemsList()){
                articulos.add(new Articulo(i));  
                logger.info("venta es en estado "+ i.getItem().getItemId());
                logger.info(" "+ i.getItem().getIsActiva());
            }
        }
        Compra compra = new Compra();
        Saldo saldo = new Saldo(billetera.getSaldo(user_id));
        logger.info("saldo buscado "+saldo.getSaldo());
        mav.addObject("saldo", saldo);
        mav.addObject("Articulos", articulos);
        mav.addObject("compra", compra);
        logger.info("se agregaron los modelos a la vista de items");
        return mav;
    }
    

    @GetMapping("/ventas")
    public ModelAndView getpublicaciones(@CookieValue(value = "nombre", defaultValue = "Atta") String nombre,
                                        @CookieValue(value = "apellido", defaultValue = "Atta") String apellido, 
                                        @CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                                        @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion
                                        ){

        ModelAndView mav = new ModelAndView(ViewRouteHelper.PUBLICACIONES);
        logger.info("nombre de usuario " +nombre);
        int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }

        ItemsCompraVentaResponse items = cliente.getItemsEnVenta(user_id);
        List<Articulo> articulos = new ArrayList<Articulo>();
        if(items != null){

            for(ItemSale i:items.getItemsList()){
                logger.info("esta venta activa "+ i.getItem().getIsActiva());
                articulos.add(new Articulo(i));  
            }
        }
        mav.addObject("Articulos", articulos);
            return mav;
    }
    

    @GetMapping("/compras")
    public ModelAndView getcompras(@CookieValue(value = "nombre", defaultValue = "Atta") String nombre,
                                        @CookieValue(value = "apellido", defaultValue = "Atta") String apellido, 
                                        @CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                                        @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion
                                        ){

        logger.info("nombre de usuario +" +nombre);
        int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            ModelAndView mav = new ModelAndView(ViewRouteHelper.PUBLICACIONES);
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }
        ModelAndView mav = new ModelAndView(ViewRouteHelper.COMPRAS);
        ItemsCompraVentaResponse items = cliente.getItemsComprados(user_id);
        List<Articulo> articulos = new ArrayList<Articulo>();
        if(items != null){

            for(ItemSale i:items.getItemsList()){
                logger.info("esta venta activa "+ i.getItem().getIsActiva());
                articulos.add(new Articulo(i));  
            }
        }
        mav.addObject("Articulos", articulos);
        return mav;
    }


    @PostMapping("/comprar/{id_item}")
    public RedirectView comprarArticulo(@CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,@ModelAttribute("compra")Compra compra,@PathVariable("id_item") int idArticulo ) {

        compra.setIdArticulo(idArticulo);
        int idUser =0;
        if(id_usuario != null && id_usuario != "Atta"){
            idUser = Integer.parseInt(id_usuario);
            compra.setIdUsuario(idUser);
            cliente.comprarArticulo(compra);
        }
        
        return new RedirectView("/items");
    }


    @GetMapping("ventas/nuevo")
    public ModelAndView getNuevoArticulo(@CookieValue(value = "nombre", defaultValue = "Atta") String nombre,
                                        @CookieValue(value = "apellido", defaultValue = "Atta") String apellido, 
                                        @CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                                        @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion
                                        ){

        logger.info("nombre de usuario +" +nombre);
        int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            ModelAndView mav = new ModelAndView(ViewRouteHelper.PUBLICACIONES);
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }

        Venta venta = new Venta();
        ImagenWrapper imagen = new ImagenWrapper();
        // ModeloImagen[] imagenes = new ModeloImagen[5];
        ModelAndView mav = new ModelAndView(ViewRouteHelper.NUEVA_PUBLICACION);
        mav.addObject("venta",venta);
        mav.addObject("imagen",imagen);
        // mav.addObject("imagen",imagenes);
        return mav;
    }
    

    @RequestMapping(value = "/ventas/submit", method = RequestMethod.POST)
    public RedirectView submitArticulos(
                            @CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                            @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion,    
                            @RequestParam("files") MultipartFile[] files, ModelMap modelMap, 
                            @ModelAttribute("venta")Venta venta) {

    modelMap.addAttribute("files", files);


    RedirectView mav = new RedirectView("/ventas");
    int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }

    int idArticulo = 0;
    for(int i = 0; i < (files.length > 5 ? 5 : files.length ); i++){

        try{
        byte [] byteArr = files[i].getBytes();
        InputStream foto = files[i].getInputStream();
        if(i == 0){
           idArticulo = cliente.cargarArticulo(foto, files[i].getOriginalFilename(), user_id, venta);
           logger.info("Cargando primera imagen, articulo quedo con id "+ idArticulo);

        }else{
            cliente.cargarImagen(foto, files[i].getOriginalFilename(), user_id, idArticulo);
            logger.info("Cargando siguientes imagenes");
        }
            
        }catch(Exception e){
            logger.info("error cargando imagen en bytes"+e.getMessage());
        }
    }
    return mav;
}


    @GetMapping("/billetera")
    public ModelAndView vistaBilletera(@CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                                        @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion){
        int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            ModelAndView mav = new ModelAndView(ViewRouteHelper.PUBLICACIONES);
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }
        ModelAndView mav = new ModelAndView(ViewRouteHelper.BILLETERA);

        Saldo saldo = new Saldo(billetera.getSaldo(user_id));
        mav.addObject("saldo", saldo);
        return mav;  
    }

    @RequestMapping(value = "/billetera", method = RequestMethod.POST)
    public RedirectView cargarBilletera(
                            @CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                            @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion,    
                            @ModelAttribute("saldo")Saldo saldo) {


    RedirectView mav = new RedirectView("/items");
    int user_id = 0;
    int sesion_id = 0;
    double importe = 0;
    logger.info("saldo a cargar "+saldo.getSaldo());
    if(id_usuario != "Atta" && id_sesion != "Atta"){
        user_id = Integer.parseInt(id_usuario);
        sesion_id = Integer.parseInt(id_sesion);
        importe = saldo.getSaldo();
    }else{
        logger.info("no se guardo el id_usuario o la sesion");
        return mav;
    }
    billetera.cargarSaldo(user_id, importe, sesion_id);

    
    return mav;
    }
}
