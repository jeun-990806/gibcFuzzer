//removexattr
#include <sys/xattr.h>
#include <stdint.h>
int target(uint8_t **data) {
	removexattr(data[0], data[1]);
	return 0;
}