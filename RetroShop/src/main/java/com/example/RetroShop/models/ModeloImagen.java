package com.example.RetroShop.models;

import org.springframework.web.multipart.MultipartFile;

public class ModeloImagen {
    private MultipartFile imagen;


    public ModeloImagen() {
    }



    public MultipartFile getImagen() {
        return this.imagen;
    }

    public void setImagen(MultipartFile imagen) {
        this.imagen = imagen;
    }


    
    
}
