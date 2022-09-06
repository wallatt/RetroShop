package com.example.RetroShop.entities;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

import com.example.RetroShop.models.Compra;
import com.example.RetroShop.models.Filtro;
import com.example.RetroShop.models.Venta;
import com.google.j2objc.annotations.ReflectionSupport.Level;
import com.google.protobuf.ByteString;
import com.google.protobuf.Timestamp;
import static java.lang.System.currentTimeMillis;

import io.grpc.RetroShop.articulo.ItemServiceGrpc.*;
import io.grpc.RetroShop.articulo.*;
import io.grpc.RetroShop.articulo.ItemServiceGrpc.ItemServiceBlockingStub;
import io.grpc.stub.StreamObserver;

import java.nio.file.Files;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;

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

    
    public Items getItems(int user_id){
        getItemsRequest request = getItemsRequest.newBuilder().setUserId(user_id).build();
        Items response;
        try{
            logger.info("intentando obtener articulos ");
            response = blockingStub.getItems(request);
        }
        catch (StatusRuntimeException e) {
            logger.info("no se pudo obtener articulos");
            return null;
        }
        return response;
    }

    
    public Items getFiltrados(Filtro filtro, int user_id){

        ItemCategory cat = ItemCategory.forNumber(Integer.parseInt(filtro.getCategoria()));
        Timestamp timestampMin;
        Timestamp timestampMax;
        try {
            timestampMin = Timestamp.newBuilder().setSeconds(filtro.getFechaMin().getTime()).build();
        } catch (Exception e) {
            timestampMin = Timestamp.newBuilder().setSeconds(0).build();
        }
        try {
            timestampMax = Timestamp.newBuilder().setSeconds(filtro.getFechaMax().getTime()).build();
        } catch (Exception e) {
            timestampMax = Timestamp.newBuilder().setSeconds(0).build();
        }
        // logger.info("timestamp max: " + timestampMax.toString());
        // logger.info("timestamp min: " + timestampMin.toString());
        // logger.info("fecha min: " + filtro.getFechaMin().toString());
        // logger.info("fecha max: " + filtro.getFechaMax().toString());
        getItemsFiltered request = getItemsFiltered.newBuilder().setUserId(user_id).setFechaDesde(timestampMin)
                        .setFechaHasta(timestampMax)
                        .setCategory(cat)
                        .setPreciomin(filtro.getPrecioMin())
                        .setPreciomax(filtro.getPrecioMax())
                        .setNombre(filtro.getNombre())
                        .build();
        Items response;
        try{
            logger.info("intentando obtener articulos filtrados ");
            response = blockingStub.getItemsFiltered(request);
        }
        catch (StatusRuntimeException e) {
            logger.info("no se pudo obtener articulos filtrados");
            return null;
        }
        return response;
    }



    public ItemsCompraVentaResponse getItemsEnVenta(int id_usuario){
        ItemsCompraVenta request = ItemsCompraVenta.newBuilder().setUserId(id_usuario).build();
        ItemsCompraVentaResponse response;
        try{
            logger.info("intentando obtener articulos ");
            response = blockingStub.itemsEnVenta(request);
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
            logger.info("no se pudo obtener imagen ");
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


    public void cargarImagen(InputStream foto, String ruta, int user_id,int item_id)throws InterruptedException{
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
            
            String nombre = String.valueOf(ruta.hashCode());

            String imagetype = ruta.substring(ruta.lastIndexOf("."));
            metadata metadatos = metadata.newBuilder().setUserId(user_id).setItemId(item_id).setNombre(nombre).setTipoImg(imagetype).build(); 
            DataChunk request = DataChunk.newBuilder().setConfiguration(metadatos).build();
    
            try{
                requestObserver.onNext(request);
    
                byte[] buffer = new byte[1024];
                while(true){
                    int n = foto.read(buffer);
                    if( n <= 0){
                        foto.close();
                        break;
                    }
                    
                    if(finishLatch.getCount() == 0){
                        foto.close();
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
    

    public int cargarArticulo(InputStream foto, String imagen, int user_id, Venta venta) throws InterruptedException{
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

            DateFormat formatter = new SimpleDateFormat("yyyy-MM-dd");
        // you can change format of date
            Date date = new Date();
            try {
                date =formatter.parse(venta.getFecha());
            } catch (Exception e) {
                // TODO: handle exception
            }
            // Timestamp timeStampDate = new Timestamp(date.getTime());
            // Timestamp timestamp = new java.sql.Timestamp(parsedDate.getTime());
        
            String nombre = String.valueOf(imagen.hashCode());
            ItemCategory cat = ItemCategory.forNumber(Integer.parseInt(venta.getCategoria()));
            Instant time = Instant.now();
            Timestamp timestamp = Timestamp.newBuilder().setSeconds(date.getTime())
            .build();

            
            Item item = Item.newBuilder().setNombre(venta.getNombre())
                                        .setDescripcion(venta.getDescripcion())
                                        .setPrecio(venta.getPrecio())
                                        .setCantidad(venta.getCantidad())
                                        .setFechaFabricacion(timestamp)
                                        .setCategory(cat)
                                        .build();
            String imagetype = imagen.substring(imagen.lastIndexOf("."));

            Itemdata metadatos = Itemdata.newBuilder()
                                .setUserId(user_id)
                                .setItemId(0)
                                .setTipoImg(imagetype)
                                .setNombre(nombre)
                                .setItem(item)
                                .build(); 
            NewItemSaleRequest request = NewItemSaleRequest.newBuilder().setConfiguration(metadatos).build();
            int articuloId =0;
            try{
                requestObserver.onNext(request);
    
                byte[] buffer = new byte[1024];
                while(true){
                    int n = foto.read(buffer);
                    if( n <= 0){
                        foto.close();
                        break;
                    }
                    
                    if(finishLatch.getCount() == 0){
                        foto.close();
                        return 0;
                    }
                    request = NewItemSaleRequest.newBuilder().setData(ByteString.copyFrom(buffer,0,n)).build();
    
                    requestObserver.onNext(request);
                    logger.info("Se envio imagen de tamano "+ n);
                }
            }catch(Exception e){
                logger.info("fallo carga "+ e.getMessage()); 
                requestObserver.onError(e);
                return 0;
            }
            requestObserver.onCompleted();
            if(!finishLatch.await(1, TimeUnit.MINUTES)){
                logger.warning("request no se completo en un minuto");
    
            }
            getItemsRequest requestId = getItemsRequest.newBuilder().setUserId(user_id).build();
            ItemId response;
            try{
                response = blockingStub.getUltimoArticuloCreado(requestId);
                articuloId = response.getItemId();
            }
            catch (StatusRuntimeException e) {
                logger.info("no se pudo obtener articulos");
                return 0;
            }
            return articuloId;


    }


    public void comprarArticulo(Compra compra){
        buyItemRequest request = buyItemRequest.newBuilder()
                                .setCantidad(compra.getCantidad())
                                .setUserId(compra.getIdUsuario())
                                .setItemId(compra.getIdArticulo())
                                .build();
        Empty response;
        try{
            response = blockingStub.comprarItem(request);
        }
        catch (StatusRuntimeException e) {
            logger.info("error al intentar comprar articulo");
        }
        
        }


    public ItemsCompraVentaResponse getItemsComprados(int user_id) {
        ItemsCompraVenta request = ItemsCompraVenta.newBuilder().setUserId(user_id).build();
        ItemsCompraVentaResponse response;
        try{
            response = blockingStub.itemsComprados(request);
        }
        catch (StatusRuntimeException e) {
            logger.info("no se pudo obtener articulos");
            return null;
        }
        return response;
    }        
        
      

        
    
    
}
