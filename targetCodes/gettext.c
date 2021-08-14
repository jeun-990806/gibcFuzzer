//gettext
#include <libintl.h>
#include <stdint.h>
int target(uint8_t **data) {
	gettext(data[0]);
	return 0;
}