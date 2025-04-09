#include "feed_manage.h"

#include "log.h"
#include "feed_protocol.h"

int fun_feed_manage_init()
{
    dal_feed_protocol_init();

    LOG("fun_feed_manage_init\n");
    return 0;
}