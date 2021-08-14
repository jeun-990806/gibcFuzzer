//isfdtype
#include <sys/stat.h>
#include <sys/socket.h>
#include <stdint.h>
int target(uint8_t **data) {
	isfdtype(data[0][0], data[1][0]);
	return 0;
}