//mkostemp
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	mkostemp(data[0], data[1][0]);
	return 0;
}