//posix_openpt
#include <stdlib.h>
#include <fcntl.h>
#include <stdint.h>
int target(uint8_t **data) {
	posix_openpt(data[0][0]);
	return 0;
}