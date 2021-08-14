//basename
#include <libgen.h>
#include <stdint.h>
int target(uint8_t **data) {
	basename(data[0]);
	return 0;
}