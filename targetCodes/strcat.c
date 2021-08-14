//strcat
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	strcat(data[0], data[1]);
	return 0;
}