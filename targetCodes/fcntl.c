//fcntl
#include <fcntl.h>
#include <stdint.h>
int target(uint8_t **data) {
	fcntl(data[0][0], data[1][0]);
	return 0;
}