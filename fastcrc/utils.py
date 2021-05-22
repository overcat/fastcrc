def _ensure_bytes(data: bytes) -> None:
    if not isinstance(data, bytes):
        raise TypeError(
            "a bytes-like object is required, not '{data_type}'".format(
                data_type=type(data).__name__
            )
        )
