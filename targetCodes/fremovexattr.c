//fremovexattr
#include <sys/xattr.h>
#include <stdint.h>
int target(uint8_t **data) {
	fremovexattr(data[0][0], data[1]);
	return 0;
}