public class Programador {
    public String nome;
    private int idade;
    public String tecnologias;

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

    public void status() {
        System.out.println("Dados sobre o novo Programador: \n");
        System.out.println("Nome: " + this.getNome());
        System.out.println("Idade: " + this.idade);
        System.out.println("Tecnologias: " + this.getTecnologias());
    }
    
}
