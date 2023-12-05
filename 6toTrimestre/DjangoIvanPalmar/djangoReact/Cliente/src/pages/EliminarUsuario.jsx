import React from "react";
import { Navigate, useNavigate, useParams } from "react-router-dom";
import { eliminacionUsuario } from '../api/usuariosApi/' 
import Swal from 'sweetalert2'

export function EliminarUsuario(){
    const params = useParams()   
    const navigate = useNavigate()
    console.log(params.numeroDocumento)
    
    eliminacionUsuario(params.numeroDocumento).
        then((response) => {
            Swal.fire({
                icon: "success",
                title: "Eliminacion Correcta",
                confirmButtonColor:'#3ed634',                
                confirmButtonText : 'Siguiente',
                text: "El usuario ha sido eliminado correctamente",            
            });
            navigate('/AgregarUsuario')
            return response
        })
        .catch((error)=>{
            Swal.fire({
                icon: "error",
                title: "Eliminacion Invalida",
                confirmButtonColor:'#3ed634',                
                confirmButtonText : 'Atras',
                text: "El usuario no ha podio ser eliminado correctamente",            
            });
            navigate('/AgregarUsuario')
            return error
    })           
}