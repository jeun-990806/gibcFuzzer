//sethostent
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	sethostent(data[0][0]);
	return 0;
}