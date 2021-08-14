//wctype
#include <wctype.h>
#include <stdint.h>
int target(uint8_t **data) {
	wctype(data[0]);
	return 0;
}