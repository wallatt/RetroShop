package com.example.RetroShop.entities;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;


import io.grpc.RetroShop.billetera.*;
import io.grpc.RetroShop.billetera.BilleteraGrpc.*;

public class BilleteraClient {

    private static final Logger logger = Logger.getLogger(BilleteraClient.class.getName());


    private final ManagedChannel channel;
    private final BilleteraBlockingStub blockingStub;

    public BilleteraClient(String host, int port){
        channel = ManagedChannelBuilder.forAddress(host,port).usePlaintext().build();
        blockingStub = BilleteraGrpc.newBlockingStub(channel);
    }

    public void shutdown() throws InterruptedException{
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    public double getSaldo(int idUsuario, int idSesion){
        saldoRequest request = saldoRequest.newBuilder().setIdUsuario(idUsuario).setIdSesion(idSesion).build();
        saldoResponse response;
        try{
            logger.info("intentando obtener saldo de usuario "+ idUsuario);
            response = blockingStub.getSaldo(request);
        }
        catch (StatusRuntimeException e) {
            return 0;
        }
        return response.getSaldo();
    }
    
    public void cargarSaldo(int idUsuario, double importe, int sesion_id){
        logger.info("cargando saldo "+ importe+" sesion "+ sesion_id + "usuario "+ idUsuario);
        cargarSaldoRequest request = cargarSaldoRequest.newBuilder()
                                    .setIdUsuario(idUsuario)
                                    .setImporte(importe)
                                    .setIdSesion(sesion_id).build();
        Empty response;
        try{
            logger.info("intentando obtener saldo de usuario "+ idUsuario);
            response = blockingStub.cargarSaldo(request);
        }
        catch (StatusRuntimeException e) {
            logger.info("No se pudo cargar saldo");
        }
    }
    public boolean puedeComprar(int idUsuario, double importe){
        puedeHacerCompraRequest request = puedeHacerCompraRequest.newBuilder().setIdUsuario(idUsuario).setImporte(importe).build();
        puedeHacerCompraResponse response;
        try{
            logger.info("intentando saber si el usuario puede costear "+ idUsuario);
            response = blockingStub.puedeHacerCompra(request);
        }
        catch (StatusRuntimeException e) {
            return false;
        }
        return response.getPuedeHacerCompra();
    }

    public void hacerCompra(int idComprador, int idVendedor, double importe){
        hacerCompraRequest request = hacerCompraRequest.newBuilder().setIdComprador(idComprador).setIdVendedor(idVendedor).setImporte(importe).build();
        Empty response;
        try{
            logger.info("intentando hacer transaccion del usuario "+ idComprador);
            response = blockingStub.hacerCompra(request);
        }
        catch (StatusRuntimeException e) {
        }
    }




    

    
    
}
