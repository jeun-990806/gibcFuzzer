//dprintf
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	dprintf(data[0][0], data[1]);
	return 0;
}