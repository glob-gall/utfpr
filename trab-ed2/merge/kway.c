#include "kway.h"

bool retorna_menor(int qnt,ENTRADA* entradas[qnt],ITEM_VENDA* saida){
  int menorId = INT_MAX;
  int menorEntrada=-1;
  
  int auxId;
  for (int i = 0; i < qnt; i++){
    auxId = entrada_proximo(entradas[i]);
    if (auxId < menorId){
      if (auxId != -1){
        menorId = auxId;
        menorEntrada = i;
      }
    }
  }
  
  if (menorEntrada==-1) return false;

  return entrada_consumir(entradas[menorEntrada], saida);
}

void kway(int qnt,ENTRADA* entradas[qnt], SAIDA* saida){
  ITEM_VENDA* aux = malloc(sizeof(ITEM_VENDA));

  while (retorna_menor(qnt,entradas,aux)){
    saida_inserir(aux,saida);
  }
  free(aux);
  printf("TODOS OS ARQUIVOS FORAM CONSUMIDOS!\n");
}