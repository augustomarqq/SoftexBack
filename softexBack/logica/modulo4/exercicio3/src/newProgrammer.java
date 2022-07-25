public class newProgrammer {
    public static void main(String[] args) {
        Programador newDev = new Programador();
        newDev.nome = "Augusto Allan";
        newDev.setIdade(26);
        newDev.tecnologias = "Javascript e Node.js";
        newDev.status();
        
        System.out.println("\n" + newDev.nome + " desenvolve em " + newDev.tecnologias + " e tem " + newDev.getIdade() + " anos");
    }
}
