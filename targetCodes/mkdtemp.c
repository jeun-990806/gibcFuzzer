//mkdtemp
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	mkdtemp(data[0]);
	return 0;
}