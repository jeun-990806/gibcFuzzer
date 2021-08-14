//mblen
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	mblen(data[0], data[1][0]);
	return 0;
}