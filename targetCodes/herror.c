//herror
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	herror(data[0]);
	return 0;
}