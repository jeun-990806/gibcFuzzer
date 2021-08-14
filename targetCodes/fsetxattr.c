//fsetxattr
#include <sys/xattr.h>
#include <stdint.h>
int target(uint8_t **data) {
	fsetxattr(data[0][0], data[1], data[2], data[3][0], data[4][0]);
	return 0;
}