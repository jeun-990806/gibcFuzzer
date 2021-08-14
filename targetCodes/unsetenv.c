//unsetenv
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	unsetenv(data[0]);
	return 0;
}