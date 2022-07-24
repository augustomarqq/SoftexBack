public class CarroTeste {    
    public static void main(String[] args) {

        //instanciando o objeto
        Carro carro1 = new Carro();

        //declarando valores aos atributos
        carro1.marca = "Honda";
        carro1.modelo = "Civic";
        carro1.ano = 2022;

        //chamando os metodos
        carro1.acelerar();
        carro1.frear();
        carro1.passarMarcha();

    }
}