//system
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	system(data[0]);
	return 0;
}