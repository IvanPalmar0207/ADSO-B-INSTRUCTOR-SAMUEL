import { useEffect, useState } from "react"
import { todosLosUsuario } from "../api/usuariosApi";
import {Link, useNavigate,useParams} from "react-router-dom";
import imagePlaya from '../static/img/playa.png';
import actualizar from '../static/img/actualizar.png';
import eliminar from '../static/img/eliminar.png';
import '../static/css/verTabla.css';
import {FooterLista} from '../components/footerListas'
import Swal from 'sweetalert2'

export function VerUsuarios(){

    const [usuarios, setUsuarios] = useState([]);    

    useEffect(() => {

        async function cargarUsuarios(){
            const response = await todosLosUsuario()
            setUsuarios(response.data)
        }
        cargarUsuarios()
    },[]);

    const navigate = useNavigate()
    const style = {
        with: '30px',
        height: '30px',
    };

    return (
        <div>
        
            <header>
                <div className="logoIzquierdo">
                    <img src={imagePlaya} alt="logoIzquierda" />
                </div>
                <h1 className="tituloEncabezado">Ver Usuarios - Hotel Pegasus</h1>
                <div className="logoIzquierdo">
                    <img src={imagePlaya} alt="logoIzquierda" />
                </div>
            </header>

            <ul>            
                <li><Link to='/AgregarUsuario' className="a">Volver</Link></li>
            </ul>

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous" />
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>            
            <table className="table">
                <thead className="table-info">
                    <tr style={{textAlign:'center'}}>
                        <th scope='col'>Numero de Documento</th>
                        <th scope='col'>Tipo. Documento</th>
                        <th scope='col'>Correo Electronico</th>
                        <th scope='col'>Nombres del Usuario</th>
                        <th scope='col'>Apellidos del Usuario</th>
                        <th scope='col'>Rol del Usuario</th>
                        <th scope='col'>Actualizar</th>
                        <th scope='col'>Eliminar</th>
                    </tr>
                </thead>     
                    <tbody>              
                        {usuarios.map( usuario =>
                        <tr key={usuario.numeroDocumento_usu} style={{textAlign:'center'}}>
                                <td>{usuario.numeroDocumento_usu}</td>
                                <td>{usuario.codigo_tpD}</td>
                                <td>{usuario.correoElectronico_usu}</td>
                                <td>{usuario.nombres_usu}</td>
                                <td>{usuario.apellidos_usu}</td>
                                <td>{usuario.codigo_rl}</td>                
                                <td>                                
                                    <a href=""><img src={actualizar} alt="imagenActualizar" style={style} /></a>
                                </td>
                                <td>
                                    <a onClick={() =>{                    
                                        const aceptarElimnar = Swal.mixin({
                                          });
                                          aceptarElimnar.fire({
                                            title: "Estas seguro?",
                                            text: "No se podra revertir la operacion",
                                            icon: "warning",
                                            showCancelButton: true,
                                            confirmButtonText: "Si, Eliminar!",
                                            confirmButtonColor:'#ff2d2d',                                                            
                                            reverseButtons: true,
                                            cancelButtonText: "No, cancelar",
                                            cancelButtonColor:'#3ed634',                
                                          }).then((result) => {
                                            if (result.isConfirmed) {                                                                                    
                                                navigate(`/EliminarUsuario/${usuario.numeroDocumento_usu}`)                                           
                                            } else if (
                                              /* Read more about handling dismissals below */
                                              result.dismiss === Swal.DismissReason.cancel
                                            ) {
                                              aceptarElimnar.fire({
                                                title: "Operacion Cancelada",
                                                text: "No se eliminara el registro seleccionado",
                                                icon: "error",
                                                confirmButtonColor:'#ff2d2d',   
                                                confirmButtonText: "Volver atras"                                                         
                                            });
                                            }
                                          });                                     
                                    }}                                                                                                          
                                    ><img src={eliminar} alt="imagenEliminar" style={style} /></a>                                                    
                                </td>
                        </tr>                        
                        )}                             
                    </tbody>
                </table>                                
            <FooterLista />
        </div>
    )
}
