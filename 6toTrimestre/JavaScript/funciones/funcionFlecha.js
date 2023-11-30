//Sin parametros
const x = () => "Hola, mi nombre es Ivan David Palmar Martinez";
console.log(x())

//Con Parametros
const saludo = nombre => `Hola, mi nombre es ${nombre}`
console.log(saludo('Lionel Messi'))

//Mas de un parametro
const saludoMas = (nombre, apellido) => `Hola, mi nombre es ${nombre} ${apellido}`
console.log(saludoMas('Goku','Martinez'))