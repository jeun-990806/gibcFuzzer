//rindex
#include <strings.h>
#include <stdint.h>
int target(uint8_t **data) {
	rindex(data[0], data[1][0]);
	return 0;
}