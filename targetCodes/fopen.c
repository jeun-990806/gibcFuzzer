//fopen
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	fopen(data[0], data[1]);
	return 0;
}