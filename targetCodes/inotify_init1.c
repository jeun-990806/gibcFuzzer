//inotify_init1
#include <sys/inotify.h>
#include <stdint.h>
int target(uint8_t **data) {
	inotify_init1(data[0][0]);
	return 0;
}