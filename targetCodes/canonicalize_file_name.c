//canonicalize_file_name
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	canonicalize_file_name(data[0]);
	return 0;
}