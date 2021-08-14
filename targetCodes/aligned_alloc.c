//aligned_alloc
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	aligned_alloc(data[0][0], data[1][0]);
	return 0;
}