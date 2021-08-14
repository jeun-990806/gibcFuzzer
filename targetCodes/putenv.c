//putenv
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	putenv(data[0]);
	return 0;
}