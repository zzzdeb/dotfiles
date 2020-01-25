#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
  int i = 0;
  int len = atoi(argv[1]);
  int prec = atoi(argv[2]);
  int full = len*prec/100;
  int empty = len-full;
  /* char *bar = malloc(len+1); */
  /* char *cur = bar; */
  /* for (i = 0; i < full; ++i) { */
    /* *cur='+'; */
    /* cur++; */
  /* } */
  /* for (i = 0; i < empty; ++i) { */
    /* *cur='-'; */
    /* cur++; */
  /* } */
  /* *cur = '\0'; */
  char *bar = malloc(2*len+1);
  char *cur = bar;
  for (i = 0; i < full; ++i) {
    *cur='=';
    cur++;
    *cur='\n';
    cur++;
  }
  for (i = 0; i < empty; ++i) {
    *cur='|';
    cur++;
    *cur='\n';
    cur++;
  }
  *cur = '\0';

/* FILLED_ITEMS=$(echo "((${ITEMS} * ${STATUS})/100 + 0.5) / 1" | bc) */
/* NOT_FILLED_ITEMS=$(echo "$ITEMS - $FILLED_ITEMS" | bc) */
/* msg=$(printf "%${FILLED_ITEMS}s" | sed "s| |${FILLED_ITEM}|g") */
/* msg=${msg}$(printf "%${NOT_FILLED_ITEMS}s" | sed "s| |${NOT_FILLED_ITEM}|g") */
  printf(bar);
  free(bar);
  return 0;
}
