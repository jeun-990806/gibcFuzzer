//sincos
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	sincos(data[0][0], data[1], data[2]);
	return 0;
}