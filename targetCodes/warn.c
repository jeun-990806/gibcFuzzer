//warn
#include <err.h>
#include <stdint.h>
int target(uint8_t **data) {
	warn(data[0]);
	return 0;
}