//strerrorname_np
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	strerrorname_np(data[0][0]);
	return 0;
}