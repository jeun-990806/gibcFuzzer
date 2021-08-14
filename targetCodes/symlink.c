//symlink
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	symlink(data[0], data[1]);
	return 0;
}