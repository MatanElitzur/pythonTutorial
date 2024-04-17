import hashlib

#string = "This is a test string."
string = """
{
    "token_expiresin": "1y",
    "tokens": [
        {
            "name": "DynatraceClient",
            "scopes": [
                "settings.write",
                "settings.read",
                "CaptureRequestData",
                "ReadConfig",
                "WriteConfig"
            ]
        },
        {
            "name": "GrafanaDashboard",
            "scopes": [
                "metrics.read",
                "entities.read",
                "problems.read",
                "events.read"
            ]
        },
        {
            "name": "apitoken",
            "scopes": [
                "metrics.ingest",
                "DataExport",
                "ReadSyntheticData",
                "ReadConfig",
                "WriteConfig",
                "CaptureRequestData",
                "metrics.read",
                "auditLogs.read",
                "syntheticLocations.read",
                "openTelemetryTrace.ingest",
                "releases.read",
                "entities.read"
            ]
        }
    ]
}
"""
md5_hash = hashlib.md5(string.encode('utf-8')).hexdigest()
print(f"MD5 hash of '{string}': {md5_hash}")