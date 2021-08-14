//bindtextdomain
#include <libintl.h>
#include <stdint.h>
int target(uint8_t **data) {
	bindtextdomain(data[0], data[1]);
	return 0;
}