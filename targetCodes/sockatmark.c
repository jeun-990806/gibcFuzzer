//sockatmark
#include <sys/socket.h>
#include <stdint.h>
int target(uint8_t **data) {
	sockatmark(data[0][0]);
	return 0;
}