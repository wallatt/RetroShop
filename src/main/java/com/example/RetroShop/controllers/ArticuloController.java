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
import com.example.RetroShop.models.ImagenWrapper;
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
        ImagenWrapper imagen = new ImagenWrapper();
        // ModeloImagen[] imagenes = new ModeloImagen[5];
        ModelAndView mav = new ModelAndView(ViewRouteHelper.NUEVA_PUBLICACION);
        mav.addObject("venta",venta);
        mav.addObject("imagen",imagen);
        // mav.addObject("imagen",imagenes);
        return mav;
    }
    
    
    // @PostMapping("ventas/submit")
    // public String getNuevoArticulo(@CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
    //                                     @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion, @ModelAttribute("venta")Venta venta                                        
    //                                     ){

    //     return " el usuario "+ id_usuario +" quiere vender " + venta;
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
    // }



// @PostMapping("/imagen/submit")
// public String submit(@ModelAttribute ModeloImagen file) {
//     logger.info("obteniendo imagen del request");

//         logger.info("Iterando las imagenes");
//         MultipartFile imagen = file.getImagen();
//         logger.info("imagen data "+ imagen.getOriginalFilename());

//         // try{
//         //     byte [] byteArr=imagen.getBytes();
//         //     InputStream foto = imagen.getInputStream();
//         //     cliente.cargarImagen(foto, imagen.getOriginalFilename());
//         //         logger.info("retorno de cargar imagen");
                
//         //     }catch(Exception e){
//         //         logger.info("error cargando imagen en bytes"+e.getMessage());
//         //     }
        
//             //  modelMap.addAttribute("files", files);
        
//             return "fileUploadView";
// }

@PostMapping("/imagen/submit")
public String submit(@ModelAttribute ImagenWrapper file) {
    logger.info("obteniendo imagen del request");

        logger.info("Iterando las imagenes");

        ArrayList<ModeloImagen> imagenes = file.getImagenes();
        logger.info("Imagenes recolectadas "+ imagenes.size());
        // logger.info("imagen data "+ imagen.getOriginalFilename());

        // try{
        //     byte [] byteArr=imagen.getBytes();
        //     InputStream foto = imagen.getInputStream();
        //     cliente.cargarImagen(foto, imagen.getOriginalFilename());
        //         logger.info("retorno de cargar imagen");
                
        //     }catch(Exception e){
        //         logger.info("error cargando imagen en bytes"+e.getMessage());
        //     }
        
            //  modelMap.addAttribute("files", files);
        
            return "fileUploadView";
}
// @PostMapping("/imagen/submit")
// public String submit(@ModelAttribute ImagenWrapper file) {
//     logger.info("obteniendo imagen del request");
    
//     ArrayList<ModeloImagen> imagenes = file.getImagenes();
//         for(int i = 0 ; i < imagenes.size(); i++){

//             logger.info("Iterando las imagenes");
//             MultipartFile imagen = imagenes.get(i).getImagen();
//             try{
//                 byte [] byteArr=imagen.getBytes();
//                 InputStream foto = imagen.getInputStream();
//                 cliente.cargarImagen(foto, imagen.getOriginalFilename());
//                 logger.info("retorno de cargar imagen");
                
//             }catch(Exception e){
//                 logger.info("error cargando imagen en bytes"+e.getMessage());
//             }
//         }
        
//         //  modelMap.addAttribute("files", files);
//     return "fileUploadView";
// }


// @RequestMapping(value = "/uploadMultiFile", method = RequestMethod.POST)
// public String submit(@RequestParam("files") MultipartFile[] files, ModelMap modelMap) {
//     modelMap.addAttribute("files", files);
//     logger.info("largo de array "+files.length);
//     logger.info("largo de array "+files[0].getOriginalFilename());
//     logger.info("largo de array "+files[1].getOriginalFilename());
//     for(int i = 0; i < files.length; i++){
//         logger.info("Nombre de imagenes"+files[i].getOriginalFilename());

//     }
//     return "fileUploadView";
// }


@RequestMapping(value = "/ventas/submit", method = RequestMethod.POST)
public String submitArticulos(
                            @CookieValue(value = "id_usuario", defaultValue = "Atta") String id_usuario,
                            @CookieValue(value = "id_sesion", defaultValue = "Atta") String id_sesion,    
                            @RequestParam("files") MultipartFile[] files, ModelMap modelMap, 
                            @ModelAttribute("venta")Venta venta) {

    modelMap.addAttribute("files", files);

    int user_id = 0;
        if(id_usuario == "Atta"){
            logger.info("no se guardo el id_usuario");
            ModelAndView mav = new ModelAndView(ViewRouteHelper.PUBLICACIONES);
            return "mav";
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
    return "fileUploadView";
}




    
    
}
