//chdir
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	chdir(data[0]);
	return 0;
}