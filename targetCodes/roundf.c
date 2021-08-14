//roundf
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	roundf(data[0][0]);
	return 0;
}