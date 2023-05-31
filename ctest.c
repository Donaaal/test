#include <stdio.h>
#include <stdlib.h>
int main() {
  int a = 0x80000000;
  printf("a=%x\n-a=%x\n\n", a, -a);
  printf("a=%d\n-a=%d\n\n", a, -a);
  if (a != 0 && a == -a) {
    printf("a!=0&&a=-a\n");
  }
  return 0;
}
