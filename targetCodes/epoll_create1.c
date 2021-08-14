//epoll_create1
#include <sys/epoll.h>
#include <stdint.h>
int target(uint8_t **data) {
	epoll_create1(data[0][0]);
	return 0;
}