//insque
#include <search.h>
#include <stdint.h>
int target(uint8_t **data) {
	insque(data[0], data[1]);
	return 0;
}