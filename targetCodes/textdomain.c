//textdomain
#include <libintl.h>
#include <stdint.h>
int target(uint8_t **data) {
	textdomain(data[0]);
	return 0;
}