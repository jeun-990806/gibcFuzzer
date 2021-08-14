//free
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	free(data[0]);
	return 0;
}