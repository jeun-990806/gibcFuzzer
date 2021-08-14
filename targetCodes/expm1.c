//expm1
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	expm1(data[0][0]);
	return 0;
}