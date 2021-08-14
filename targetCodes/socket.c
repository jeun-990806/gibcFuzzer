//socket
#include <sys/socket.h>
#include <stdint.h>
int target(uint8_t **data) {
	socket(data[0][0], data[1][0], data[2][0]);
	return 0;
}