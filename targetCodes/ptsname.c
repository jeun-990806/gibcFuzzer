//ptsname
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	ptsname(data[0][0]);
	return 0;
}