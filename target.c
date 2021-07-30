#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data){
	return printf(data[0]);
}
char *targetInfo(void){ return "printf";}
