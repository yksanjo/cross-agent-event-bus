from datetime import datetime, timezone


def main() -> None:
    print("cross-agent-event-bus initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
