//cbrtl
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	cbrtl(data[0][0]);
	return 0;
}