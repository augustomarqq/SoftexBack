public class AlunosTeste extends SoftexAlunos{
    public static void main(String[] args) {
        
        //declarando objeto 1
        SoftexAlunos aluno1 = new SoftexAlunos();
        aluno1.nome = "Augusto";
        aluno1.curso = "Back-End";
        totalAlunos = alunos++;

        System.out.println("O nome do novo aluno é " + aluno1.nome + " e ele está aprendendo " + aluno1.curso);
        System.out.println("O total de alunos agora é: " + alunos);

         //declarando objeto 2
         SoftexAlunos aluno2 = new SoftexAlunos();
         aluno2.nome = "Camilla";
         aluno2.curso = "Front-End";
         totalAlunos = alunos++;

         System.out.println("O nome do novo aluno é " + aluno2.nome + " e ele está aprendendo " + aluno2.curso);
         System.out.println("O total de alunos agora é: " + alunos);

         //declarando objeto 3
         SoftexAlunos aluno3 = new SoftexAlunos();
         aluno3.nome = "Guilherme";
         aluno3.curso = "Back-End";
         totalAlunos = alunos++;

         System.out.println("O nome do novo aluno é " + aluno3.nome + " e ele está aprendendo " + aluno3.curso);
         System.out.println("O total de alunos agora é: " + alunos);



       

    }
     
    
    
}
