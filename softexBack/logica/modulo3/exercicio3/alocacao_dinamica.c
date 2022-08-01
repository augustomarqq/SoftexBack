/*

Se a memória alocada dinamicamente for insuficiente ou mais do que o necessário,
você pode alterar o tamanho da memória alocada anteriormente usando a função realloc()

*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr, i, n1, n2;

    printf("Informe o tamanho: ");
    scanf("%i", &n1);

    ptr = (int*) malloc(n1 * sizeof(int)); //alocou espaço na memória

    printf("Endereço de memória alocado\n");

    for(i = 0; i < n1; i++)

        printf("%u\n", ptr + i);

    printf("Informe o novo tamanho: ");
    scanf("%i", &n2);

    ptr = realloc(ptr, n2 * sizeof(int)); //alocou novo espaço na memória (no caso, é só colocar n2=22 que teremos um vetor de tamanho 22)

    printf("Novo endereço alocado na memória\n");
    
    for (i = 0; i < n2; i++)

        printf("%u\n", ptr + i);


    free(ptr);

    return 0;
}