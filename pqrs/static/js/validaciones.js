anonimo = document.getElementById('anonimo')
titulo = document.getElementById('titulo')
correo = document.getElementById('correo')
barrio = document.getElementById('barrio')

anonimo.addEventListener('click', function(e) {
    if (anonimo.checked == true) {
        titulo.setAttribute('disabled', 'true')
        correo.setAttribute('disabled', 'true')
        barrio.setAttribute('disabled', 'true')
        
    }else{
        titulo.removeAttribute('disabled')
        correo.removeAttribute('disabled')
        barrio.removeAttribute('disabled')     
    }
})


