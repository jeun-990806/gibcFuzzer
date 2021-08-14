//getservbyname
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	getservbyname(data[0], data[1]);
	return 0;
}