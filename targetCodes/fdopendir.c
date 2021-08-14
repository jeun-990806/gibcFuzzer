//fdopendir
#include <sys/types.h>
#include <dirent.h>
#include <stdint.h>
int target(uint8_t **data) {
	fdopendir(data[0][0]);
	return 0;
}