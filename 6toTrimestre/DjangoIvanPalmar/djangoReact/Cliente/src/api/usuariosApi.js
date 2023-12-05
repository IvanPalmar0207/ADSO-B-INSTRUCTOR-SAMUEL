import axios from 'axios'

export const todosLosUsuario = () => {
    return axios.get('http://127.0.0.1:8000/usuariosAPI/usuarios/usuarios/')
}

export const agregarUsuarios = (usuarios) => {
    return axios.post('http://127.0.0.1:8000/usuariosAPI/usuarios/usuarios/', usuarios)
      .then(response => {
        console.log('Solicitud POST exitosa:', response.data);
        return response.data;
      })
      .catch(error => {
        console.error('Error en la solicitud POST:', error);
        throw error;
      });
  };

export const eliminacionUsuario = (numeroDoc) => {
    return axios.delete(`http://127.0.0.1:8000/usuariosAPI/usuarios/usuarios/${numeroDoc}`)
    .then((response) => {
      console.log('Se ha eliminado correctamente')
      return response.data
    })
    .catch((error) => {
      console.log('Hubo un error al momento de la eliminacion')
      return error
    })
}