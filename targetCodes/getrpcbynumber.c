//getrpcbynumber
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	getrpcbynumber(data[0][0]);
	return 0;
}