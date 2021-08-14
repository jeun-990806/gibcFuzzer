//lgammaf
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	lgammaf(data[0][0]);
	return 0;
}