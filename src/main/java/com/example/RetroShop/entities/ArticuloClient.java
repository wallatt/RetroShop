package com.example.RetroShop.entities;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

import io.grpc.RetroShop.articulo.ItemServiceGrpc;
import io.grpc.RetroShop.articulo.ItemServiceGrpc.*;
import io.grpc.RetroShop.articulo.*;
import io.grpc.RetroShop.articulo.ItemServiceGrpc.ItemServiceBlockingStub;

public class ArticuloClient {

    private static final Logger logger = Logger.getLogger(ArticuloClient.class.getName());

    private final ManagedChannel channel;
    private final ItemServiceBlockingStub blockingStub;
    private final ItemServiceStub stub;

    public ArticuloClient(String host, int port){
        channel = ManagedChannelBuilder.forAddress(host,port).usePlaintext().build();
        blockingStub = ItemServiceGrpc.newBlockingStub(channel);
        stub = ItemServiceGrpc.newStub(channel);
    }

    public void shutdown() throws InterruptedException{
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    public ItemSale getItem(int id_articulo, int user_id){
        ItemId request = ItemId.newBuilder().setItemId(id_articulo).setUserId(user_id).build();
        ItemSale response;
        try{
            logger.info("intentando obtener articulo "+ id_articulo);
            response = blockingStub.getItem(request);
            logger.info("quiza se obtubo articulo "+ id_articulo);
        }
        catch (StatusRuntimeException e) {
            logger.info("no se pudo "+ id_articulo);
            return null;
        }
        return response;
    }

    public byte[] getImage(String foto){
        ArrayList<String> lista_fotos = new ArrayList<String>();
        lista_fotos.add(foto);
        DownloadProductImageRequest request = DownloadProductImageRequest.newBuilder().addNombreImagen(foto).build();
        Iterator<DataChunk> response;
        ArrayList<byte[]> bytes = new ArrayList<byte[]>();

        logger.info("request creada");
        try{
            logger.info("intentando obtener foto ");
            response = blockingStub.downloadProductImage(request);
            while(response.hasNext()) {
                DataChunk chunk = response.next();
                if (chunk.hasConfiguration()) {
                    System.out.println(chunk.getConfiguration().toString());
                }else{
                    bytes.add(chunk.getData().toByteArray());
                }
             }
             byte[] bytesresponse = new byte[bytes.size()*1024];
             int i = 0;
             for(byte[] b : bytes){
                for(byte bitbit: b){
                    bytesresponse[i] = bitbit;
                 i++; 
                }
             }
             return bytesresponse;

        }
        catch (StatusRuntimeException e) {
            logger.info("no se pudo ");
            // return null;
        }
        return null;
        
       
        
        
         


    }



    
}
