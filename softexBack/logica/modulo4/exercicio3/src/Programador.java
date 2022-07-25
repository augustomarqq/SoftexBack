public class Programador {
    public String nome;
    private int idade;
    public String tecnologias;
    public boolean aprovado;


    //metodo construtor
    public Programador(String n, String t, int i) {
        this.nome = n;
        this.tecnologias = t;
        this.idade = i;
        this.estagio();
    }

    public String getNome() {
        return this.nome;
    }
    public void setNome(String m) {
        this.nome = m;
    }

    public int getIdade() {
        return this.idade; 
    }
    public void setIdade(int i) {
        this.idade = i;
    }

    public String getTecnologias() {
        return this.tecnologias;
    }
    public void setTecnologias(String m) {
        this.tecnologias = m;
    }

    public void estagio() {
        this.aprovado = true;
    }

    public void sobre(){
        System.out.println("Dados sobre o(s) novo(s) Programador(es): \n");        
    }

    public void status() {        
        System.out.println("Nome: " + this.getNome());
        System.out.println("Idade: " + this.idade);
        System.out.println("Tecnologias: " + this.getTecnologias());
        System.out.println("Aluno aprovado para o estágio: " + this.aprovado);
    }
    
}
