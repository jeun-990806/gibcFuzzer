//write
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	write(data[0][0], data[1], data[2][0]);
	return 0;
}