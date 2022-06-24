intents = [
      {
        "tag": "saludo",
        "patterns": [
          "Hola",
          "Hey",
          "Hay alguien ahi?",
          "Buen dia"
        ],
        "responses": "Hola, puedo ayudarte en algo? :)"
      },
      {
        "tag": "adios",
        "patterns": ["Adios", "Nos vemos", "Hasta luego"],
        "responses": "Nos vemos despues",
      },
      {
        "tag": "gracias",
        "patterns": ["Gracias", "Muchas gracias", "Gracias por la ayuda"],
        "responses": "Me alegra haberte ayudado"
      },
      {
        "tag": "estado",
        "patterns": ["Como estas?", "Estas bien?", "Como te sientes?"],
        "responses": "Estoy muy bien, gracias por preguntar <3"
      },
      {
        "tag": "matricula",
        "patterns": ["Quiero saber informacion de matricula", "Matriculas"],
        "responses": "Dime que quieres saber sobre las matriculas, el costo de matricula? la direccion para recoger la matricula? es toda la informacion que puedo ofrecerte :)"
      },
      {
        "tag": "pre_matricula",
        "patterns": ["Cuanto cuesta la matricula", "precio matricula", "costo matricula"],
        "responses": "El costo de la matricula es de 25 bs"
      },
      {
        "tag": "dir_matricula",
        "patterns": ["A que direccion puedo recoger la matricula?", "direccion de matricula"],
        "responses": "Claro! Aqui tienes la direccion para comprar tu matricula <a href='https://goo.gl/maps/uSkweGYEPjfp8Tan6'>Direccion de Ciudadela universitaria</a>"
      }
    ]