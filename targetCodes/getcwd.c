//getcwd
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	getcwd(data[0], data[1][0]);
	return 0;
}