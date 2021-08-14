//lremovexattr
#include <sys/xattr.h>
#include <stdint.h>
int target(uint8_t **data) {
	lremovexattr(data[0], data[1]);
	return 0;
}