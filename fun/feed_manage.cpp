#include "feed_manage.h"

#include "log.h"
#include "feed_protocol.h"

int fun_feed_manage_init()
{
    dal_feed_protocol_init();

    // 内存泄漏：分配内存但未释放
    int *ptr = new int[10];

    // 越界访问
    ptr[10] = 1;

    LOG("fun_feed_manage_init\n");
    return 0;
}