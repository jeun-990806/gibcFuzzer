//srand48
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	srand48(data[0][0]);
	return 0;
}