//tmpnam
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	tmpnam(data[0]);
	return 0;
}