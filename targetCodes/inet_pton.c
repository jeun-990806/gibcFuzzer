//inet_pton
#include <arpa/inet.h>
#include <stdint.h>
int target(uint8_t **data) {
	inet_pton(data[0][0], data[1], data[2]);
	return 0;
}