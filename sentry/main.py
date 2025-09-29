import sentry_sdk

sentry_sdk.init(
    dsn="https://1057630478ee506db2cef879e89c5a17@o4510102369140736.ingest.de.sentry.io/4510102380740688",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

if __name__ == "__main__":
    sentry_sdk.capture_message("🔔 Test event: Hello from Python!")
    try:
        1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        print("Ошибка отправлена в Sentry")
