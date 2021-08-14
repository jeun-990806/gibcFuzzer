//setkey
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	setkey(data[0]);
	return 0;
}