class YATLRequestError(Exception):
    """Raised when an HTTP request fails due to a newtwork-level error.
    
    This is exception wraps lower-level transport errors (such as timeouts
    and connection failures) into a single domain-specific exception, providing
    a clear and user-friendly error message.
    """