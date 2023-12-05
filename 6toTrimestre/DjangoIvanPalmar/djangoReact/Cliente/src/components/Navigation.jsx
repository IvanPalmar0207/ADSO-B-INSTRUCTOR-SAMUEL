import {Link} from "react-router-dom"
import '../static/css/navegacion.css'
import imagePlaya from '../static/img/playa.png'
import imageSpa from '../static/img/spa.jpg'
import {Footer} from "./footer";

export function Navigation(){
    return (    

        <body>

            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css" />
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous"/>
            <title>HOTEL PEGASUS</title>

        <header>
            <div class="logoIzquierdo">
                <img src={imagePlaya} alt="logoIzquierda" />
            </div>
            <h1 class="tituloEncabezado">HOTEL PEGASUS</h1>
            <div class="logoIzquierdo">
                <img src={imagePlaya} alt="logoIzquierda" />
            </div>
        </header>
    
        <div class="contenedorEnlaces">
            <ul>
                <li><a href="">Iniciar Sesion</a></li>
                <li><Link to='/AgregarUsuario' className="a">Gestion de Usuarios</Link></li>
                <li><a href="">Gestion de Habitaciones</a></li>
                <li><a href="">Gestion de Servicios</a></li>
            </ul>    
        </div>
    
        <section class="descripcionContenido">
            <div class="contenedorDescripcion">
                <h2><i class="bi bi-airplane-engines-fill"></i>PODRAS DISFRUTAR DE LA MEJOR COMPAÑIA<i class="bi bi-airplane-engines-fill"></i></h2>
                <div class="componentesDescripcion">
                    <div class="textoDescripcion">
                        <p>El Hotel Pegasus es un oasis de elegancia y comodidad que desafía la imaginación. Ubicado en un escenario pintoresco en las faldas
                            de las majestuosas montañas del Valle de Serenidad, este hotel es un verdadero refugio de lujo. Desde el momento en que pones un pie en el vestíbulo,
                            te sumerges en un mundo de encanto y sofisticación.
    
                            La arquitectura del Hotel Pegasus combina elementos contemporáneos con un toque de la antigua Grecia, evocando la sensación de estar en un palacio de los dioses.
                            Las columnas esculpidas, los mosaicos relucientes y las esculturas mitológicas que decoran los espacios comunes te transportan a un mundo mágico.
                            Las habitaciones son santuarios de relajación y opulencia. Cada una de las habitaciones y suites está diseñada con una paleta de colores suaves y lujosos tejidos que te envuelven en un confort celestial.
                            Desde los balcones privados, podrás disfrutar de vistas panorámicas de los verdes valles y los picos nevados que se elevan hacia el cielo.
                        </p>
                    </div>
                    <div class="imagenDescripcion">
                        <img src={imageSpa} alt="imagenSpa" width="100px" height="100px" />
                    </div>
                </div>
            </div>
        </section>    
        <Footer />
    </body>
    
    )
}
