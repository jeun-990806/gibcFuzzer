//inet_addr
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdint.h>
int target(uint8_t **data) {
	inet_addr(data[0]);
	return 0;
}