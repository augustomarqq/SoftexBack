public class AlunoTeste {
    public static void main(String[] args) {
        
        //instanciando o objeto
        Aluno aluno1 = new Aluno();

        //declarando valores aos atributos
        aluno1.nome = "Augusto Allan";
        aluno1.idade = 26;
        aluno1.curso = "Análise e Desenvolvimento de Sistemas";

        //chamando os metodos
        aluno1.assistirAula();
        aluno1.fazerProva();
        aluno1.calcularNota();

    }
}
