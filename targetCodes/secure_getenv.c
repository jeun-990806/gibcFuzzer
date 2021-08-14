//secure_getenv
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	secure_getenv(data[0]);
	return 0;
}