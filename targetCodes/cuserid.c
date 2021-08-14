//cuserid
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	cuserid(data[0]);
	return 0;
}