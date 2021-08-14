//opendir
#include <dirent.h>
#include <stdint.h>
int target(uint8_t **data) {
	opendir(data[0]);
	return 0;
}