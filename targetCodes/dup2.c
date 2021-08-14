//dup2
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	dup2(data[0][0], data[1][0]);
	return 0;
}