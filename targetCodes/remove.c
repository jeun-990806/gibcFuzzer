//remove
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	remove(data[0]);
	return 0;
}