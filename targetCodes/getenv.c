//getenv
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	getenv(data[0]);
	return 0;
}