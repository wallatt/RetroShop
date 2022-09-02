package com.example.RetroShop.entities;

import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

import io.grpc.RetroShop.helloworld.*;

/**
 * A simple client that requests a greeting from the {@link HelloWorldServer}.
 */
public class HelloWorldClient {
    
    public HelloWorldClient() {
        this.channel = ManagedChannelBuilder.forTarget("localhost:50051").usePlaintext().build();
        try{
            this.blockingStub = activarCliente(this.channel);
        }catch(Exception e){
            this.blockingStub = null;
        }
        
    }

     
    private ManagedChannel channel;
    private GreeterGrpc.GreeterBlockingStub blockingStub;

    public String greet(String name) {
        HelloRequest request = HelloRequest.newBuilder().setName(name).build();
        HelloReply response;
        try {
            response = blockingStub.sayHello(request);
        } catch (StatusRuntimeException e) {
            return null;
        }
        return response.getMessage();
    }

    public GreeterGrpc.GreeterBlockingStub activarCliente(ManagedChannel channel) throws Exception {
        try {
            return GreeterGrpc.newBlockingStub(channel);
        } finally {}
    }

    public void shutdown(){
        try{
        this.channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        }catch (InterruptedException e){ }
    }
}


