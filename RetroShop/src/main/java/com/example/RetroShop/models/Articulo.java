package com.example.RetroShop.models;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Objects;

import org.springframework.boot.autoconfigure.domain.EntityScan;

import io.grpc.RetroShop.articulo.ItemSale;

@EntityScan
public class Articulo{
    public ItemSale item;
    public String fecha;
    
    public Articulo(ItemSale item){
        this.item = item;
        fecha = this.setFecha(item);
    }

    String setFecha(ItemSale item){
        String fecha = item.getItem().getFechaFabricacion().toString();
        long segundos = Long.parseLong(((fecha.substring(fecha.lastIndexOf(":")).replace(":","").replace(" ","").replace("\n",""))));
        Date date = new Date(segundos*1000);
        SimpleDateFormat dateformatter = new SimpleDateFormat("dd MMM yyyy");
        fecha = dateformatter.format(date);
        return fecha;
    }
    
    public String getFecha(){
        return this.fecha;
    }

    public Articulo() {
    }

    public Articulo(ItemSale item, String fecha) {
        this.item = item;
        this.fecha = fecha;
    }

    public ItemSale getItem() {
        return this.item;
    }

    public void setItem(ItemSale item) {
        this.item = item;
    }



    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Articulo)) {
            return false;
        }
        Articulo articulo = (Articulo) o;
        return Objects.equals(item, articulo.item) && Objects.equals(fecha, articulo.fecha);
    }

    @Override
    public int hashCode() {
        return Objects.hash(item, fecha);
    }

    @Override
    public String toString() {
        return "{" +
            " item='" + getItem() + "'" +
            ", fecha='" + getFecha() + "'" +
            "}";
    }


}
