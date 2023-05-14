#include <stdio.h>
#include "hello.h"
int fab(int n);
int jiecheng(int n);
int main(){
  printf("0.1+0.2=%f\n",0.1+0.2);
  printf("fab(6)=%d\nfactorial(6)=%d\n",fab(8),factorial(8));
  return 0;
}
//斐波那契：
int fab(int n){
  if(n==1||n==2){
    return 1;
  }
  return fab(n-1)+fab(n-2);
}
//阶乘：
int factorial(int n){
  if(n==1){
    return 1;
  }
  return n*factorial(n-1);
}
