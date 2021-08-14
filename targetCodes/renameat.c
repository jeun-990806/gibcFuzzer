//renameat
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	renameat(data[0][0], data[1], data[2][0], data[3]);
	return 0;
}