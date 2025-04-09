#include "log.h"
#include "feed_protocol.h"
#include "feed_manage.h"

int main()
{
    LOG("hello world\n");

    fun_feed_manage_init();

    while (1)
        ;
    return 0;
}