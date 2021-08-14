//getdents64
#include <dirent.h>
#include <stdint.h>
int target(uint8_t **data) {
	getdents64(data[0][0], data[1], data[2][0]);
	return 0;
}