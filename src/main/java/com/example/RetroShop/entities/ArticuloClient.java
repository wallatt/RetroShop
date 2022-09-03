package com.example.RetroShop.entities;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

import com.google.j2objc.annotations.ReflectionSupport.Level;
import com.google.protobuf.ByteString;
import com.google.protobuf.Timestamp;
import static java.lang.System.currentTimeMillis;

import io.grpc.RetroShop.articulo.ItemServiceGrpc;
import io.grpc.RetroShop.articulo.ItemServiceGrpc.*;
import io.grpc.RetroShop.articulo.*;
import io.grpc.RetroShop.articulo.ItemServiceGrpc.ItemServiceBlockingStub;
import io.grpc.stub.StreamObserver;

import java.nio.file.Files;
import java.time.Instant;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

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

    public Items getItems(){
        getItemsRequest request = getItemsRequest.newBuilder().setUserId(1).build();
        Items response;
        try{
            logger.info("intentando obtener articulos ");
            response = blockingStub.getItems(request);
            logger.info("quiza se obtubieron articulos ");
        }
        catch (StatusRuntimeException e) {
            logger.info("no se pudo obtener articulos");
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
        }
        return null;
    }


    public void subirImagen(String ruta, int user_id, int item_id) throws InterruptedException{
        final CountDownLatch finishLatch = new CountDownLatch(1);


        StreamObserver<DataChunk> requestObserver = 
        stub.withDeadlineAfter(5, TimeUnit.SECONDS)
        .uploadProductImage(new StreamObserver<UploadProductResponse>() {
            @Override
            public void onNext(UploadProductResponse response){
                logger.info("receive response: \n" + response);
            }
            @Override
            public void onError(Throwable t){
                logger.info("Upload fallo " + t);
                finishLatch.countDown();
            }

            @Override
            public void onCompleted(){
                logger.info("Image Uploaded ");
                finishLatch.countDown();
            }
            
        });

        FileInputStream fileInputStream;
        try{
            fileInputStream = new FileInputStream(ruta);
            String nombre = String.valueOf(ruta.hashCode());

            String imagetype = ruta.substring(ruta.lastIndexOf("."));
            metadata metadatos = metadata.newBuilder().setUserId(user_id).setItemId(item_id).setNombre(nombre).setTipoImg(imagetype).build(); 
            DataChunk request = DataChunk.newBuilder().setConfiguration(metadatos).build();
    
            try{
                requestObserver.onNext(request);
    
                byte[] buffer = new byte[1024];
                while(true){
                    int n = fileInputStream.read(buffer);
                    if( n <= 0){
                        fileInputStream.close();
                        break;
                    }
                    
                    if(finishLatch.getCount() == 0){
                        fileInputStream.close();
                        return;
                    }
                    request = DataChunk.newBuilder().setData(ByteString.copyFrom(buffer,0,n)).build();
    
                    requestObserver.onNext(request);
                    logger.info("Se envio imagen de tamano "+ n);
                }
            }catch(Exception e){
                logger.info("fallo carga "+ e.getMessage()); 
                requestObserver.onError(e);
                return;
            }
            requestObserver.onCompleted();
            if(!finishLatch.await(1, TimeUnit.MINUTES)){
                logger.warning("request no se completo en un minuto");
    
            }
        }catch(FileNotFoundException e){
            logger.info("imagen no encontrada "+ e.getMessage());
            return;
        }
    }


    public void nuevoArticulo(String ruta, int user_id, String articulo, String desc, double precio, int cant) throws InterruptedException{
        final CountDownLatch finishLatch = new CountDownLatch(1);

        StreamObserver<NewItemSaleRequest> requestObserver = 
        stub.withDeadlineAfter(5, TimeUnit.SECONDS)
        .nuevoItemSaleRequest(new StreamObserver<ItemId>() {
            @Override
            public void onNext(ItemId response){
                logger.info("receive response: \n" + response);
            }
            @Override
            public void onError(Throwable t){
                logger.info("Upload fallo " + t);
                finishLatch.countDown();
            }

            @Override
            public void onCompleted(){
                logger.info("Image Uploaded ");
                finishLatch.countDown();
            }
            
        });

        FileInputStream fileInputStream;
        try{
            fileInputStream = new FileInputStream(ruta);
            String nombre = String.valueOf(ruta.hashCode());
            ItemCategory cat = ItemCategory.valueOf("HOGAR");
            Instant time = Instant.now();
            Timestamp timestamp = Timestamp.newBuilder().setSeconds(time.getEpochSecond())
            .build();
            
            Item item = Item.newBuilder().setNombre(articulo)
                                        .setDescripcion(desc)
                                        .setPrecio(precio)
                                        .setCantidad(cant)
                                        .setFechaFabricacion(timestamp)
                                        .setCategory(cat)
                                        .build();
            String imagetype = ruta.substring(ruta.lastIndexOf("."));

            Itemdata metadatos = Itemdata.newBuilder()
                                .setUserId(user_id)
                                .setItemId(0)
                                .setTipoImg(imagetype)
                                .setNombre(nombre)
                                .setItem(item)
                                .build(); 
            NewItemSaleRequest request = NewItemSaleRequest.newBuilder().setConfiguration(metadatos).build();
    
            try{
                requestObserver.onNext(request);
    
                byte[] buffer = new byte[1024];
                while(true){
                    int n = fileInputStream.read(buffer);
                    if( n <= 0){
                        fileInputStream.close();
                        break;
                    }
                    
                    if(finishLatch.getCount() == 0){
                        fileInputStream.close();
                        return;
                    }
                    request = NewItemSaleRequest.newBuilder().setData(ByteString.copyFrom(buffer,0,n)).build();
    
                    requestObserver.onNext(request);
                    logger.info("Se envio imagen de tamano "+ n);
                }
            }catch(Exception e){
                logger.info("fallo carga "+ e.getMessage()); 
                requestObserver.onError(e);
                return;
            }
            requestObserver.onCompleted();
            if(!finishLatch.await(1, TimeUnit.MINUTES)){
                logger.warning("request no se completo en un minuto");
    
            }
        }catch(FileNotFoundException e){
            logger.info("imagen no encontrada "+ e.getMessage());
            return;
        }


    }

     
    
}
