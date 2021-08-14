//getprotobyname
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	getprotobyname(data[0]);
	return 0;
}