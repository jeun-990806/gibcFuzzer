//rename
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	rename(data[0], data[1]);
	return 0;
}