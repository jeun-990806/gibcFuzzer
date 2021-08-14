//open
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>
int target(uint8_t **data) {
	open(data[0], data[1][0]);
	return 0;
}