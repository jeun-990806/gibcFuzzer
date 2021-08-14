//iconv_open
#include <iconv.h>
#include <stdint.h>
int target(uint8_t **data) {
	iconv_open(data[0], data[1]);
	return 0;
}