//dgettext
#include <libintl.h>
#include <stdint.h>
int target(uint8_t **data) {
	dgettext(data[0], data[1]);
	return 0;
}