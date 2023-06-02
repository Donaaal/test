#include <stdio.h>
#include <stdlib.h>
int getSize(int k){
  if(k==0){
    return 1;
  }
  int size=0;
  while(k!=0){
    size++;
    k/=10;
  }
  return size;
}
int *getNums(int k){
  int size=getSize(k);
  int* nums=(int *)calloc(size, sizeof(int));
  for (int i=size-1; i>=0; i--) {
    nums[i]=k%10;
    k/=10;
  }
  return nums;
}
char* DigiTran(int k){
  int size=getSize(k);
  char* res=(char*)calloc(size,sizeof(char));
  int *nums=getNums(k);
  int i=0;
  int j=0;
  while(i<size){
    if(i==size-1){
      res[j]='A'+nums[i];
      break;
    }
    int tmp=nums[i]*10+nums[i+1];
    if(tmp<26){
      res[j]='A'+tmp;
      j++;
      i+=2;
    }
    else {
      res[j]='A'+nums[i];
      j++;
      i++;
    }
  }
  return res;
}
int main() {
  int k;
  char* res=NULL;
  scanf("%d",&k);
  if(k==-1){exit(0);}
  while(k!=-1){
    getNums(k);
    res=DigiTran(k);
    printf("%s ",res);
    scanf("%d",&k);
  }
  printf("\n");
  return 0;
}
