package com.example.RetrosShop.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

// import com.example.demo.cliente.*;
// import java.util.logging.Logger;


@RestController
public class Controller {

    @GetMapping("/")
    public String holamundo(){

        // HelloWorldClient hello = new HelloWorldClient();

        // String resultado = hello.greet("walter");

        // Logger logger = Logger.getLogger(Controller.class.getName());

        // logger.info("Hola"+ resultado);



        return "holamundo baba " ;//+ resultado;
    }
}
