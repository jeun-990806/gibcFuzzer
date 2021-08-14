//rpmatch
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	rpmatch(data[0]);
	return 0;
}