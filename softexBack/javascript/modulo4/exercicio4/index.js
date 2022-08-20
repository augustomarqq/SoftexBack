const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Welcome to my app")
})

app.get("/about", (req, res) => {
    res.send("If you can feel you heartbeat, you're not done, you can't be.")
})

app.get("/contact", (req, res) => {
    res.send("E-mail: augustomarx@gmail.com")
})

app.listen(8082, () => {
    console.log("Servidor hospedado na URL http://localhost:8082");
    console.log("Pressione ctrl + c para desligar o servidor")
});