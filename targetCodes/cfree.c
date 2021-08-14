//cfree
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	cfree(data[0]);
	return 0;
}