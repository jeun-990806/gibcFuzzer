//setstate
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	setstate(data[0]);
	return 0;
}