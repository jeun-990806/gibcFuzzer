//linkat
#include <fcntl.h>
#include <stdint.h>
int target(uint8_t **data) {
	linkat(data[0][0], data[1], data[2][0], data[3], data[4][0]);
	return 0;
}