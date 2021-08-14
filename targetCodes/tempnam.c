//tempnam
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	tempnam(data[0], data[1]);
	return 0;
}