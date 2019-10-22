# kafka-demo-py
Demo Using Kafka with Python

Producer/Consumer comunicando entre si Utilizando Apache Kafka, em Python.

# Subir a Aplicacao com Docker:
  Acesse a raiz do repositorio e rode: 
  
```  
  make docker  
```

  Parar a Aplicacao: make dockerdown  

  Para mais detalhes: make help  

# Dependencias

Flask, kafka-python, pytest, flask-swagger-ui

# Requisitos :

Deixar as Porta (8080, 8081, 9092) do seu host local livre, pois serão essas portas que as aplicacões irao utilizar.

# Fluxo de Inicialização da Aplicacao

 1. Baixa as images da DockerHub;
 2. Docker Faz o Build da Imagem do Python com o Fonte da Aplicacao;
 3. Docker-Compose sobe uma stack com os Containers necessario de Cada API;
 
# Endereços e Servicos

No Navegador acesse: 

Producer API = http://127.0.0.1:8080/api-docs

Consumer API = http://127.0.0.1:8081/api-docs

# Links/Observações

Para Utilizar Docker é necessario ter instalado:

```  
  Docker: https://www.docker.com/

  Docker-Compose: https://docs.docker.com/compose/
  
```  

# Referencias

https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f

https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05

