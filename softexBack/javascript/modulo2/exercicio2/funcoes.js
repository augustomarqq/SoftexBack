
export function somar(a, b){
    return console.log("A soma de "+ a +" + "+ b +" = "+ (a + b))
};

export function subtrair(a, b){
    return console.log("A subtração de "+ a +" - "+ b +" = "+ (a - b))
};

export function multiplicar(a, b){
    return console.log("A multiplicação de "+ a +" * "+ b +" = "+ (a * b))
};

export function dividir(a, b){
    if (a%b == 0)
    return console.log("A divisão de "+ a +" / "+ b +" = "+ (a / b))
    else
    return console.log("A divisão de "+ a +" / "+ b +" = "+ (a / b) +" e a sobra foi "+ a%b)
};