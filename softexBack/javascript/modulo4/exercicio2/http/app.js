//import express from "express";

var express = require('express');

const app = express();

app.listen(8084, () => {
  console.log("Servidor de pé em http://localhost:8084")
  console.log("Para desligar o servidor: ctrl + c")
});

// rotas
app.get('/', (req ,res) =>{    
    res.send("<h1>Home</h1>");
});

app.get('/user', (req, res) =>{
    res.send(`
        <h1>Usuário<h1>
        
        <form action="/user" method="POST">
            <label for="email">E-mail:</label>
            <input type="email" name="email" id="email">
            <label for="mensagem">Mensagem:</label>
            <textarea name="mensagem" id="mensagem"></textarea>
            <input type="submit" value="Enviar">
        </form>
    `)
});

app.post('/user', (req, res) => {
    res.send("<h1>Mensagem enviada com sucesso!</h1>");
  });