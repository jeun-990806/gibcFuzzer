//tcgetsid
#include <termios.h>
#include <stdint.h>
int target(uint8_t **data) {
	tcgetsid(data[0][0]);
	return 0;
}