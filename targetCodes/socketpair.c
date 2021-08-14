//socketpair
#include <sys/socket.h>
#include <stdint.h>
int target(uint8_t **data) {
	socketpair(data[0][0], data[1][0], data[2][0], data[3][0]);
	return 0;
}