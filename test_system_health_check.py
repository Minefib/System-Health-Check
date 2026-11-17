from system_health_check import diskSpace, ramUsage, uptime

def test_disk_space_is_valid():
    total_size, used_size, free_size, percent_size = diskSpace("/")
    
    assert 0 <= percent_size <= 100
    assert used_size <= total_size


def test_ram_usage_is_valid():
    ramUsed, ramTotal, ramPercent, ramFree = ramUsage()

    assert 0 <= ramPercent <= 100
    assert ramUsed <= ramTotal

def test_uptime_is_valid():
    hours, minutes = uptime()

    assert hours >= 0
    assert 0 <= minutes < 60

