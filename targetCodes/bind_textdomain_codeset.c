//bind_textdomain_codeset
#include <libintl.h>
#include <stdint.h>
int target(uint8_t **data) {
	bind_textdomain_codeset(data[0], data[1]);
	return 0;
}