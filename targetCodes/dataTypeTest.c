#include <stdint.h>
#include <stdio.h>

int target(uint8_t **data){
	short oneByte = data[0][0];
	char character = data[3][0];
	int fourBytes = data[1][0];
	long eightBytes = data[2];
	printf("ok!\n");
	return 0;
}
