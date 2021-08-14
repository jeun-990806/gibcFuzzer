//mktemp
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	mktemp(data[0]);
	return 0;
}