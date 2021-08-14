//wctrans
#include <wctype.h>
#include <stdint.h>
int target(uint8_t **data) {
	wctrans(data[0]);
	return 0;
}