//strfromf
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	strfromf(data[0], data[1][0], data[2], data[3][0]);
	return 0;
}