package com.example.RetroShop.models;

import java.util.ArrayList;
import java.util.Date;

public class Venta {
    private String nombre;
    private String descripcion;
    private String categoria;
    private String fecha;
    private int cantidad;
    private double precio;
    private ArrayList<String> fotos;


    public Venta() {
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


    public String getDescripcion() {
        return this.descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
   

    public String getCategoria() {
        return this.categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public String getFecha() {
        return this.fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public int getCantidad() {
        return this.cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public double getPrecio() {
        return this.precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public ArrayList<String> getFotos() {
        return this.fotos;
    }

    public void setFotos(ArrayList<String> fotos) {
        this.fotos = fotos;
    }

    @Override
    public String toString() {
        return "{" +
            " nombre='" + getNombre() + "'" +
            ", getDescripcion='" + getDescripcion() + "'" +
            ", categoria='" + getCategoria() + "'" +
            ", fecha='" + getFecha() + "'" +
            ", cantidad='" + getCantidad() + "'" +
            ", precio='" + getPrecio() + "'" +
            ", fotos='" + getFotos() + "'" +
            "}";
    }




    
}
