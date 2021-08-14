//getservbyport
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	getservbyport(data[0][0], data[1]);
	return 0;
}