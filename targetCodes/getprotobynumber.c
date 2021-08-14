//getprotobynumber
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	getprotobynumber(data[0][0]);
	return 0;
}