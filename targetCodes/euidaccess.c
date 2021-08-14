//euidaccess
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	euidaccess(data[0], data[1][0]);
	return 0;
}