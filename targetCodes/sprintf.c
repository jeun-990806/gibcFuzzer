//sprintf
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	sprintf(data[0], data[1]);
	return 0;
}