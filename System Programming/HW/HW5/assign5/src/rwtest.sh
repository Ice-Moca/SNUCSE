#!/bin/bash

# Default port number
PORT=8080

# Parse arguments for port number (optional)
while getopts "p:" opt; do
    case $opt in
        p) PORT=$OPTARG ;;
        *) echo "Usage: $0 [-p port] [1|2|3|4]"; exit 1 ;;
    esac
done

# Shift so that $1 now points to the test set selection (if provided)
shift $((OPTIND-1))

if [ -z "$1" ]; then
    echo "Usage: $0 [-p port] [1|2|3|4]"
    exit 1
fi

TEST_SET=$1

# Select the REQUESTS, RESPONSES, and INTERVALS based on the test set number
case $TEST_SET in
    1)
        REQUESTS=(
            "CREATE hello 1"
            "CREATE hello 2"
            "CREATE hello 3"
            "CREATE hello 4"
        )
        RESPONSES=(
            "CREATE OK"
            "COLLISION"
            "COLLISION"
            "COLLISION"
        )
        INTERVALS=(5 5 5 5)
        ;;
    2)
        REQUESTS=(
            "CREATE hello world"
            "READ hello"
            "READ hello"
            "READ hello"
        )
        RESPONSES=(
            "CREATE OK"
            "world"
            "world"
            "world"
        )
        INTERVALS=(5 5 0 0)
        ;;
    3)
        REQUESTS=(
            "CREATE hello world"
            "READ hello"
            "CREATE bye snu"
            "READ bye"
        )
        RESPONSES=(
            "CREATE OK"
            "world"
            "CREATE OK"
            "snu"
        )
        INTERVALS=(5 5 -5 5)
        ;;
    4)
        REQUESTS=(
            "CREATE hello world"
            "DELETE bye"
            "READ hello"
            "UPDATE hello snu"
            "DELETE hello"
            "READ hello"
        )
        RESPONSES=(
            "CREATE OK"
            "NOT FOUND"
            "world"
            "UPDATE OK"
            "DELETE OK"
            "world"
        )
        INTERVALS=(5 0 5 5 5 -10)
        ;;
    *)
        echo "Invalid test set number. Use 1, 2, 3, or 4."
        exit 1
        ;;
esac

OUTPUT_DIR="./output"
if [[ -d $OUTPUT_DIR ]]; then
    rm -rf $OUTPUT_DIR
fi
mkdir -p $OUTPUT_DIR

echo "=== Starting Requests and Responses (Test Set $TEST_SET) ==="

START_TIME=$(date +%s)
RESPONSE_TIMES=()

# Run each request in the background and record the response time in the log file
for i in "${!REQUESTS[@]}"; do
    echo "Sending Request $i: '${REQUESTS[$i]}'"
    {
        # Send the request through the client
        echo "${REQUESTS[$i]}" | ./client -p $PORT | ts '[%Y-%m-%d %H:%M:%S]' > "$OUTPUT_DIR/response_$i.log"
        # Record UNIX timestamp at the end of the log file
        date +%s >> "$OUTPUT_DIR/response_$i.log"
    } &
    # A slight delay to ensure proper ordering
    sleep 0.1
done

# Wait for all background processes to finish
wait

echo "=== Verifying Responses ==="

# Function to check if the expected response string is present in the log file
check_required_string() {
    local file=$1
    local string=$2
    if ! grep -q "$string" "$file"; then
        echo -e "\033[31mError: Expected '$string' not found in $file\033[0m"
        return 1
    fi
    return 0
}

# Validate the responses
for i in "${!REQUESTS[@]}"; do
    echo "Checking response for Request $i..."
    check_required_string "$OUTPUT_DIR/response_$i.log" "${RESPONSES[$i]}" || {
        echo -e "\033[31mTest Failed: '${RESPONSES[$i]}' missing in response_$i.log\033[0m"
        exit 1
    }
    echo "Response for Request $i: '${RESPONSES[$i]}' verified successfully."
done

echo "=== Extracting Recorded Timestamps ==="

# Extract the recorded timestamp (last line of each response file) into RESPONSE_TIMES
for i in "${!REQUESTS[@]}"; do
    RESPONSE_TIMES[$i]=$(tail -n 1 "$OUTPUT_DIR/response_$i.log")
done

echo "=== Calculating Response Time Differences ==="

# Check time intervals between responses
for ((i = 1; i < ${#RESPONSE_TIMES[@]}; i++)); do
    diff=$((RESPONSE_TIMES[$i] - RESPONSE_TIMES[$((i - 1))]))
    expected_interval="${INTERVALS[$i]}"
    echo "Response $((i - 1)) to Response $i: $diff seconds (expected: $expected_interval seconds)"

    # Allow ±1 second deviation
    if [[ $diff -lt $((expected_interval - 1)) || $diff -gt $((expected_interval + 1)) ]]; then
        echo -e "\033[31mTest Failed: Time difference between Response $((i - 1)) and Response $i is not in the $((expected_interval - 1))-$((expected_interval + 1)) seconds range\033[0m"
        exit 1
    fi
done

echo -e "\033[32mTest Passed: All conditions satisfied for Test Set $TEST_SET.\033[0m"
exit 0
