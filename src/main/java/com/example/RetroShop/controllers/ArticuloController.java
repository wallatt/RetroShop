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
import com.example.RetroShop.helper.ViewRouteHelper;
import com.example.RetroShop.models.Articulo;
import com.example.RetroShop.models.Compra;
import com.example.RetroShop.models.ModeloImagen;
import com.example.RetroShop.models.Venta;
import com.google.protobuf.Timestamp;

import io.grpc.RetroShop.articulo.ItemSale;
import io.grpc.RetroShop.articulo.Items;
import io.grpc.RetroShop.articulo.ItemsCompraVentaResponse;

import java.io.FileInputStream;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;
import java.util.logging.Logger;

import javax.servlet.http.HttpServletRequest;



@RestController
public class ArticuloController {

    ArticuloClient cliente = new ArticuloClient("localhost", 50052);

    Logger logger = Logger.getLogger(ArticuloController.class.getName());

    @ResponseBody
    @RequestMapping(value = "/fotos/{id_foto}", method = RequestMethod.GET, produces = MediaType.IMAGE_PNG_VALUE)
    public byte[] getfoto(@PathVariable String id_foto){
        logger.info("Resolviendo imagen request");

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
    public ModelAndView getItem(@PathVariable("id_item") int id){
        ModelAndView mav = new ModelAndView(ViewRouteHelper.ARTICULO);
        ItemSale item = cliente.getItem(id, 2);

        Compra compra = new Compra();
 
        mav.addObject("compra", compra);
        mav.addObject("Articulo", item);
        return mav;
    }
    
    @GetMapping("/items")
    public ModelAndView getItems(){
        ModelAndView mav = new ModelAndView(ViewRouteHelper.ARTICULOS);
        Items items = cliente.getItems();
        List<Articulo> articulos = new ArrayList<Articulo>();
        for(ItemSale i:items.getItemsList()){
            articulos.add(new Articulo(i));  
            logger.info("venta es en estado "+ i.getItem().getItemId());
            logger.info(" "+ i.getItem().getIsActiva());
        }
        Compra compra = new Compra();
        compra.setCantidad(25);
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
        logger.info("nombre de usuario +" +nombre);
        int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            return mav;
        }else{
            user_id = Integer.parseInt(id_usuario);
        }

        ItemsCompraVentaResponse items = cliente.getItemsEnVenta(user_id);
        List<Articulo> articulos = new ArrayList<Articulo>();
        for(ItemSale i:items.getItemsList()){
            logger.info("esta venta activa "+ i.getItem().getIsActiva());
            articulos.add(new Articulo(i));  
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
        for(ItemSale i:items.getItemsList()){
            logger.info("esta venta activa "+ i.getItem().getIsActiva());
            articulos.add(new Articulo(i));  
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
        ModeloImagen imagen = new ModeloImagen();
        ModelAndView mav = new ModelAndView(ViewRouteHelper.NUEVA_PUBLICACION);
        mav.addObject("venta",venta);
        mav.addObject("imagen",imagen);
        return mav;
    }
    
    
    @PostMapping("ventas/submit")
    public String getNuevoArticulo(@CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                                        @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion, @ModelAttribute("venta")Venta venta                                        
                                        ){

        return " el usuario "+ id_usuario +" quiere vender " + venta;
        // logger.info(" el usuario "+ id_usuario +" quiere vender " + venta);
        // int user_id = 0;
        // if(id_usuario == "Atta"){
        //     logger.info("no se guardo el id_usuario");
        //     ModelAndView mav = new ModelAndView(ViewRouteHelper.PUBLICACIONES);
        //     return mav;
        // }else{
        //     user_id = Integer.parseInt(id_usuario);
        // }

        // Venta venta = new Venta();
        // ModelAndView mav = new ModelAndView(ViewRouteHelper.NUEVA_PUBLICACION);
        // mav.addObject("venta",venta);
        // return mav;
    }

    // @PostMapping("/imagen/submit")
    // public String imagen (){
    //     return "se cargo la imagen";
    // }

//     @PostMapping("/imagen/submit")
//     public String submit(@ModelAttribute ModeloImagen modeloImagen, ModelMap modelMap) {

//         MultipartFile file = modeloImagen.getImagen();
//         // byte [] byteArr=file.getBytes();
        
//         logger.info("file + "+file.getOriginalFilename());
//         modelMap.addAttribute("modeloImagen", modeloImagen);
//         return "fileUploadView";
// }


//     @RequestMapping(value = "/imagen/submit", method = RequestMethod.POST)
//     public String submit(@RequestParam("file") MultipartFile file, ModelMap modelMap) {

//         // MultipartFile file = modeloImagen.getImagen();
//         // byte [] byteArr=file.getBytes();
//         logger.info("obteniendo el mapping de imagen");
//         logger.info("file + "+file.getOriginalFilename());
//         // modelMap.addAttribute("modeloImagen", file);
//         return "file + "+file.getOriginalFilename();
// }

@PostMapping("/imagen/submit")
public String submit(@ModelAttribute ModeloImagen file) {
    logger.info("obteniendo imagen del request");

         MultipartFile imagen = file.getImagen();
         try{
             byte [] byteArr=imagen.getBytes();
             InputStream foto = imagen.getInputStream();
             cliente.cargarImagen(foto, imagen.getOriginalFilename());
             logger.info("retorno de cargar imagen");
 

         }catch(Exception e){
            logger.info("error cargando imagen en bytes"+e.getMessage());
         }
        //  modelMap.addAttribute("files", files);
    return "fileUploadView";
}




    
    
}
