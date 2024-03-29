//Criando um objeto com no mínimo 3 propriedades e listando-as

//Objeto
var timesFutebol = {
    serieA:"palmeiras",
    serieB:"nautico", 
    serieC:"remo",
    serieD:"santa cruz"
};

//Para prop (propriedade) in timesFutebol (objeto) faça
let listaPropriedades = () => {
for (var prop in timesFutebol) {
  // ctrl+shift+k (para abrir o console no mozilla firefox)
  console.log(prop + " = " + timesFutebol[prop]);
};
};


//Criando um array com no mínimo 3 elementos e listando-os.

//Array
let alunos = ["augusto", "guilherme", "camilla", "susy"];

//Para nomes (elementos) in alunos (array) faça
let listaElementos = () => {
for (const nomes of alunos) {
  console.log("aluno = " + nomes);
};
};

listaPropriedades()
console.log("\n")
listaElementos()