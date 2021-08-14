//scalbnl
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	scalbnl(data[0][0], data[1][0]);
	return 0;
}