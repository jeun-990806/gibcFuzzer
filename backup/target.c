#include <stdio.h>
#include <stdint.h>

int target(uint8_t **data){
	printf("%s", data[0]);
	return 0;
}

const char *targetInfo(void){
	return "printf";
}
