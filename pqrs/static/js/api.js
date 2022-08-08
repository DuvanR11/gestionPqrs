selectBarrio = document.getElementById('barrio')

fetch('https://www.datos.gov.co/resource/jtbk-heuv.json')
  .then(response => response.json())
  .then(data =>  {
    for(let i in data){
       
        opcion = `<option>${data[i].barrio}</option>`
        selectBarrio.innerHTML += opcion
        console.log(data[i].barrio);
    }
    });