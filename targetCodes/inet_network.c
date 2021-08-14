//inet_network
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdint.h>
int target(uint8_t **data) {
	inet_network(data[0]);
	return 0;
}