//ether_aton
#include <netinet/ether.h>
#include <stdint.h>
int target(uint8_t **data) {
	ether_aton(data[0]);
	return 0;
}