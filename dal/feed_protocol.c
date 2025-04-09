#include "feed_protocol.h"

#include "log.h"
#include "uart.h"

int dal_feed_protocol_init()
{
    hal_uart_init();

    LOG("dal_feed_protocol_init\n");
    return 0;
}