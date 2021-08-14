//realpath
#include <limits.h>
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	realpath(data[0], data[1]);
	return 0;
}