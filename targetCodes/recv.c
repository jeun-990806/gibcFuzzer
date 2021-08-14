//recv
#include <sys/socket.h>
#include <stdint.h>
int target(uint8_t **data) {
	recv(data[0][0], data[1], data[2][0], data[3][0]);
	return 0;
}