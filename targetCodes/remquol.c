//remquol
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	remquol(data[0][0], data[1][0], data[2]);
	return 0;
}