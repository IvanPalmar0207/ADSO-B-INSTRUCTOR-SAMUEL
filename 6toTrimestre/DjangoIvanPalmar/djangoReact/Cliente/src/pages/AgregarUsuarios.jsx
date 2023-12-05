import React, { useEffect, useState } from "react";
import {Link} from "react-router-dom";
import { ListarRoles } from "../api/rolesAPI";
import { ListarTiposDocumento } from "../api/tiposDocumentoAPI"
import '../static/css/agregarUsuario.css'
import imagePlaya from '../static/img/playa.png'
import { useForm } from "react-hook-form";
import { agregarUsuarios } from "../api/usuariosApi";
import {useNavigate } from "react-router-dom";
import {Footer} from "../components/footer";
import Swal from 'sweetalert2'

export function AgregarUsuario(){

    const [roles, setRoles] = useState([])
    const [tiposDoc, setTiposDoc] = useState([])
    const [valorSelectTipo, setValorSelectTipo] = useState("");
    const [valorSelectRol, setValoRol] = useState("");


    useEffect(()=>{

        async function listarRoles(){
            const response = await ListarRoles()
            setRoles(response.data)
        }
        listarRoles()
    },[])

    useEffect(() => {
        async function listarTipoDocumento(){
            const response = await ListarTiposDocumento();
            setTiposDoc(response.data)
        }
        listarTipoDocumento()
    },[])

    const {register, handleSubmit, formState: errors} = useForm();

    const navigate = useNavigate();

    const handleChangeSelect = (event) => {
        setValorSelectTipo(event.target.value);
      };
    
    const handleChangeSelectRol = (event) => {
        setValoRol(event.target.value);
    };
    

    const envioForm = handleSubmit(async (data) => {
        try {
            const valorFormulario = {
                ...data,
                codigo_tpD : valorSelectTipo,
                codigo_rl : valorSelectRol            
            }

            Swal.fire({
                icon: "success",
                title: "Registro Correcto",
                confirmButtonColor:'#3ed634',                
                confirmButtonText : 'Siguiente',
                text: "El usuario ha sido ingresado correctamente",            
            });
            await agregarUsuarios(valorFormulario);        
            navigate('/');
        } catch (error) {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                confirmButtonColor:'#ff3333',                
                confirmButtonText : 'Volver',
                text: "Hubo un problema ingresando el usuario!",
                footer: 'Uno de los campos es incorrecto, trata nuevamente'
            });
            console.error('Error al agregar usuarios:', error);
        }
      });

    return (
        
            <div>                        
                <header>
                

                    <div className="logoIzquierdo">
                        <img src={imagePlaya}alt="logoIzquierda" />
                    </div>
                    <h1 className="tituloEncabezado">Registrate con Pegasus</h1>
                    <div className="logoIzquierdo">
                        <img src={imagePlaya} alt="logoIzquierda" />
                    </div>
                </header>

                <div className="contenedorEnlaces">
                    <ul>
                        <li><Link to='/' className="a">Volver</Link></li>
                        <li><Link to='/ListaUsuarios' className="a">Ver Usuarios</Link></li>                       
                    </ul>   
                </div>

                <section className="formRegistro">
                    <form className="contenedor" onSubmit={envioForm} >
                        
                        <div className="campo">
                            <label htmlFor="numeroDoc">Numero de Documento:</label>
                            <input type="number" name="numeroDoc" id="numeroDoc" required
                            {...register("numeroDocumento_usu", {required : true})}                    
                            />
                            {errors.numeroDocumento_usu && <span>El campo es obligatorio</span>}
                        </div>
                    

                        <br />

                        <div className ="campo">
                            <label htmlFor="tipoDoc">Tipo de Documento:</label>
                            <select className="input" name="tipoDoc" id="tipoDoc" required                  
                            {...register("tipoDocumento_usu", {required : true})}                                      
                            value = {valorSelectTipo}
                            onChange={handleChangeSelect}                
                            >        
                            <option></option>
                            {tiposDoc.map(tipo =>
                                    <option key={tipo.codigo_tpD} value={tipo.codigo_tpD}>{tipo.tipo_tpDD}</option>
                            )}
                            </select >
                            {errors.tipoDocumento_usu && <span>El campo es obligatorio</span>}        
                        </div>

                        <br />

                        <div className="campo">
                            <label htmlFor="email">Correo Electronico: </label>
                            <input type="email" name="email" id="email" required 
                            {...register("correoElectronico_usu", {required : true})}                                                
                            />
                            {errors.correoElectronico_usu && <span>El campo es obligatorio</span>}        
                        </div>

                        <br />

                        <div className="campo">
                            <label htmlFor="nombre">Nombres del usuario:</label>
                            <input type="text" name="nombre" id="nombre" required 
                            {...register("nombres_usu", {required : true})}                                                
                            />
                            
                        </div>
                        {errors.nombres_usu && <span>El campo es obligatorio</span>}        
                        <br />

                        <div className="campo">
                            <label htmlFor="apellido">Apellidos del usuario:</label>
                            <input type="text" name="apellido" id="apellido" required 
                            {...register("apellidos_usu", {required : true})}                                                
                            />
                        {errors.apellidos_usu && <span>El campo es obligatorio</span>}                                
                        </div>

                        <br />

                        <div className="campo">
                            <label htmlFor="rol">Rol de usuario:</label>
                            <select className="input" name="rol" id="rol" required 
                            {...register("rol_usu", { required: true })}
                            value = {valorSelectRol}
                            onChange={handleChangeSelectRol}
                            >                
                            <option></option>
                            {roles.map(rol =>
                                    <option key={rol.codigo_rl} value={rol.codigo_rl}>{rol.tipo_rl}</option>
                            )}
                            </select>
                            {errors.rol_usu && <span>El campo es obligatorio</span>}                                
                        </div>

                        <br />

                        <div className="campo">
                            <label htmlFor="contrasena">Contraseña del usuario:</label>
                            <input type="password" name="contrasena" id="contrasena" required 
                            {...register("contrasena_usu", {required : true})}                                                
                            />
                            {errors.contrasena_usu && <span>El campo es obligatorio</span>}                                
                        </div>

                        <br />

                        <button className="boton">Ingresa</button>
                        <br/>
                            <Link to={'/'}>Ya tienes cuenta?</Link>
                        <br/>    
                    </form>                            
                </section>
                <Footer />
            </div>    
        )
}