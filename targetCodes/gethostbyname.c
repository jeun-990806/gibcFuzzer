//gethostbyname
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	gethostbyname(data[0]);
	return 0;
}