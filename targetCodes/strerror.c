//strerror
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	strerror(data[0][0]);
	return 0;
}