//gai_strerror
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	gai_strerror(data[0][0]);
	return 0;
}