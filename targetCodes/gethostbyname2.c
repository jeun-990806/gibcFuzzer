//gethostbyname2
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	gethostbyname2(data[0], data[1][0]);
	return 0;
}