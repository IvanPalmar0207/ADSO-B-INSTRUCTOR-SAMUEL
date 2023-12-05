import {BrowserRouter, Route, Routes, Navigate} from "react-router-dom";
import { AgregarUsuario } from './pages/AgregarUsuarios';
import { Navigation } from "./components/Navigation";
import { ListaUsuarios } from './pages/ListarUsuarios';
import {EliminarUsuario} from './pages/EliminarUsuario'

function App() {

  return (  
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigation />} />
        <Route path="/ListaUsuarios" element={<ListaUsuarios />} />        
        <Route path="/AgregarUsuario" element={<AgregarUsuario />} />
        <Route path="/EliminarUsuario/:numeroDocumento" element={<EliminarUsuario />} />
      </Routes>          
    </BrowserRouter>
  )
}

export default App