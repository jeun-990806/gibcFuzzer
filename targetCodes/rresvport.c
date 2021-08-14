//rresvport
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	rresvport(data[0]);
	return 0;
}