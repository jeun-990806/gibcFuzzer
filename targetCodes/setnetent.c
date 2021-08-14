//setnetent
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	setnetent(data[0][0]);
	return 0;
}