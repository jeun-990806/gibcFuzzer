//dirname
#include <libgen.h>
#include <stdint.h>
int target(uint8_t **data) {
	dirname(data[0]);
	return 0;
}