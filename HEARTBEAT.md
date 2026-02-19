# HEARTBEAT.md - Health Check Tasks

## Scheduled Tasks

### 1. OpenClaw Health Monitor
- **Frequency**: Every hour (0 * * * *)
- **Next Run**: Check cron status
- **Action**: Monitor OpenClaw status and restart gateway if needed
- **Script**: /Users/gudaiping/.openclaw/workspace/scripts/openclaw_monitor.sh
- **Log**: /tmp/openclaw_monitor.log

## Manual Checks (When Heartbeat Fires)

If this file is read during a heartbeat, perform the following checks:

1. Check if any cron tasks are due
2. Check if OpenClaw gateway is responsive
3. Check system resources (optional)

If OpenClaw is not responding:
- Attempt to restart gateway: openclaw gateway restart
- Log the incident

## Current Status

Last Updated: 2026-02-12 01:19 GMT+8
Status: OK
