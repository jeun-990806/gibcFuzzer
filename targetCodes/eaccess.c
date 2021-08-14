//eaccess
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	eaccess(data[0], data[1][0]);
	return 0;
}