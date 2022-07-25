public class newProgrammer {
    public static void main(String[] args) {
        Programador newDev = new Programador("Augusto Allan", "Javascript/Node.js", 26); 
        newDev.sobre(); 
        newDev.status();
        System.out.println("\n" + newDev.nome + " desenvolve em " + newDev.tecnologias + " e tem " + newDev.getIdade() + " anos \n");

        Programador newDev2 = new Programador("Rodrigo Lima", "Java/Spring", 28);
        newDev2.status();        
        System.out.println("\n" + newDev2.nome + " desenvolve em " + newDev2.tecnologias + " e tem " + newDev2.getIdade() + " anos");
    }
}
