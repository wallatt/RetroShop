package com.example.RetroShop.models;

public class Usuario {

    private String nombre;
    private String apellido;
	private String mail;
	private String password;
	private int dni;
    private String usuario;


    public Usuario() {
    }
    

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return this.apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getMail() {
        return this.mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }

    public String getPassword() {
        return this.password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public int getDni() {
        return this.dni;
    }

    public void setDni(int dni) {
        this.dni = dni;
    }

    public String getUsuario() {
        return this.usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }


    @Override
    public String toString() {
        return "{" +
            " nombre='" + getNombre() + "'" +
            ", apellido='" + getApellido() + "'" +
            ", mail='" + getMail() + "'" +
            ", password='" + getPassword() + "'" +
            ", dni='" + getDni() + "'" +
            ", usuario='" + getUsuario() + "'" +
            "}";
    }




    
    
}
