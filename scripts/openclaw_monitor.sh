#!/bin/bash
# OpenClaw Health Monitor Script
# Checks if OpenClaw is running normally and restarts gateway if needed

LOG_FILE="/tmp/openclaw_monitor.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Function to log messages
log_message() {
    echo "[$TIMESTAMP] $1" >> "$LOG_FILE"
}

log_message "Starting OpenClaw health check..."

# Check if openclaw command is available
if ! command -v openclaw &> /dev/null; then
    log_message "ERROR: openclaw command not found"
    exit 1
fi

# Check OpenClaw status
STATUS_OUTPUT=$(openclaw status 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    log_message "WARNING: OpenClaw status check failed with exit code $EXIT_CODE"
    log_message "Output: $STATUS_OUTPUT"
    
    # Try to restart gateway
    log_message "Attempting to restart OpenClaw gateway..."
    RESTART_OUTPUT=$(openclaw gateway restart 2>&1)
    RESTART_EXIT=$?
    
    if [ $RESTART_EXIT -eq 0 ]; then
        log_message "SUCCESS: Gateway restarted successfully"
        log_message "Restart output: $RESTART_OUTPUT"
        
        # Send notification (optional)
        if command -v osascript &> /dev/null; then
            osascript -e 'display notification "OpenClaw gateway restarted" with title "OpenClaw Monitor"'
        fi
    else
        log_message "ERROR: Gateway restart failed with exit code $RESTART_EXIT"
        log_message "Restart output: $RESTART_OUTPUT"
    fi
else
    log_message "INFO: OpenClaw is running normally"
fi

# Keep log file size manageable (max 1000 lines)
if [ -f "$LOG_FILE" ]; then
    tail -n 1000 "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
fi

exit 0
