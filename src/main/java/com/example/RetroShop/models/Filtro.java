package com.example.RetroShop.models;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import ch.qos.logback.classic.Logger;

public class Filtro {
    String categoria;
    String nombre;
    double precioMax;
    double precioMin;
    Date fechaMin;
    Date fechaMax;


    public Filtro() {
    }

    public Filtro(String nombre, String categoria, String precioMin, String precioMax, String fechaMin, String fechaMax) {
        this.nombre = nombre == null ? "" : nombre;
        this.categoria = categoria == null ? "" : categoria;
        setPrecioMin(precioMin);
        setPrecioMax(precioMax);
        setFechas(fechaMin, fechaMax);
        setPrecios();
    }

    public void setFechas(String fechaMin, String fechaMax) {  

       if(fechaMin != null){
        DateFormat formatter1 = new SimpleDateFormat("yyyy-MM-dd");
            try {
                Date date1 = new Date();
                date1 = formatter1.parse(fechaMin);
                this.fechaMin = date1;
            } catch (Exception e) {
        }
       }
       if(fechaMax != null){
        DateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
            try {
                Date date = new Date();
                date = formatter.parse(fechaMax);     
                this.fechaMax = date;
            } catch (Exception e) {
        }
       }
       if(this.fechaMax != null && this.fechaMin != null){
        if(this.fechaMax.before(this.fechaMin)){
            this.fechaMax = null;
        }
       }
       

    }

    public void setPrecios(){
        if(this.precioMax > 0 && this.precioMin > this.precioMax){
            this.precioMax = 0;
        }
    }

    public void setPrecioMin(String precioMin) {
        if(precioMin == null){
            this.precioMin = 0.0;
        }else{
            try {
                this.precioMin = Double.parseDouble(precioMin);
            }catch(Exception e){
                this.precioMin = 0.0;
            }
        }
    }
    
    public void setPrecioMax(String precioMax) {
        if(precioMax == null){
            this.precioMax = 0.0;
        
        }else{
            try {
                this.precioMax = Double.parseDouble(precioMax);
            }catch(Exception e){
                this.precioMax = 0.0;
            }
            }

    }


    public String getCategoria() {
        return this.categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecioMax() {
        return this.precioMax;
    }

    public void setPrecioMax(double precioMax) {
        this.precioMax = precioMax;
    }

    public double getPrecioMin() {
        return this.precioMin;
    }

    public void setPrecioMin(double precioMin) {
        this.precioMin = precioMin;
    }


    public Date getFechaMax() {
        return this.fechaMax;
    }
    public Date getFechaMin() {
        return this.fechaMin;
    }




    
}
