package com.example.RetroShop.controllers;

import com.example.RetroShop.entities.ArticuloClient;
import com.example.RetroShop.entities.BilleteraClient;
import com.example.RetroShop.entities.UsuarioClient;

public class Clientes{
    
    public static final BilleteraClient billetera = new BilleteraClient("localhost", 50053);
    public static final ArticuloClient articulo = new ArticuloClient("localhost", 50052);
    public static final UsuarioClient usuario = new UsuarioClient("localhost", 50051);

    
}
