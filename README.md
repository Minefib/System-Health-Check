# System Health Check

![Tests](https://github.com/Minefib/system_Health_Check/actions/workflows/tests.yml/badge.svg)

A small Python script that prints the health of a Linux machine: disk usage, RAM usage and uptime. It warns when the disk is more than 90% full.

This is a learning project. It is tested with pytest, checked automatically by GitHub Actions on every push, and can run inside a Docker container.

## Example output

```
Disk usage: 351.11 GB / 989.34 GB (35%)
Disk free space: 587.9 GB
Ram usage: 11.77 GB / 16.0 GB (74%)
Ram free: 4.23 GB
Uptime: 4h 13m
```

If the disk is above 90%, a warning line is printed first. Your numbers will differ.

## Requirements

- Python 3.8 or newer
- The packages in `requirements.txt` (`psutil`, `pytest`)

## Run it

```
pip install -r requirements.txt
python system_health_check.py
```

## Run the tests

```
python -m pytest
```

The tests check rules that must always be true, for example: the disk percent is between 0 and 100, used space is not bigger than total space, and minutes of uptime are below 60.

## Run it in Docker

```
docker build -t health-check .
docker run --rm health-check
```

Note: inside a container, the disk numbers describe the container's own filesystem. RAM and uptime come from the host machine's kernel.

## Continuous integration

On every push and pull request, GitHub Actions installs the requirements and runs the tests (`.github/workflows/tests.yml`). The badge at the top shows the latest result.

## Project structure

```
system_health_check.py        the script
test_system_health_check.py   pytest tests
requirements.txt              Python dependencies
Dockerfile                    container recipe
.dockerignore                 files Docker should skip
.github/workflows/tests.yml   CI workflow
```

## Known limitations

- Made for Linux. The disk path is hardcoded to `/`.
- Sizes are shown in decimal GB (1 GB = 1,000,000,000 bytes), so they can differ slightly from tools that use GiB.
- The tests check value ranges, not exact calculations.
- The script prints once and exits. It does not run on a schedule or send alerts.

## Possible improvements

- Take the disk path and the warning threshold as command-line arguments.
- Add exact-value tests for the percent and uptime calculations.
- Output JSON so other tools can read the results.
- Run on a schedule and send an alert when a limit is crossed.
