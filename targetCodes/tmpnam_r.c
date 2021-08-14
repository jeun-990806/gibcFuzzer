//tmpnam_r
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	tmpnam_r(data[0]);
	return 0;
}