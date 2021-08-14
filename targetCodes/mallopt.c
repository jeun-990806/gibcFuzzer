//mallopt
#include <malloc.h>
#include <stdint.h>
int target(uint8_t **data) {
	mallopt(data[0][0], data[1][0]);
	return 0;
}