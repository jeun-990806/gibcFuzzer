//log1p
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	log1p(data[0][0]);
	return 0;
}