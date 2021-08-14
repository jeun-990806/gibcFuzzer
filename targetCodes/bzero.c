//bzero
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	bzero(data[0], data[1][0]);
	return 0;
}