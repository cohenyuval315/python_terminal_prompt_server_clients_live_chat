import enum
class StatusCodes(enum.Enum):
    STATUS_OK = 200
    STATUS_CREATED = 201

    STATUS_NOT_MODIFIED = 304
    STATUS_BAD_REQUEST = 400
    STATUS_UNAUTHORIZED = 401
    STATUS_NOT_FOUND = 404
    STATUS_METHOD_NOT_ALLOWED = 405
    STATUS_FORBIDDEN = 403
    STATUS_CONFLIC = 409
    STATUS_TOO_MANY_REQUESTS = 429
    STATUS_INTERNAL_SERVER_ERROR = 500

    SUCCESS_STATUS_CODES = [
        STATUS_CREATED,
        STATUS_OK
    ]    
    ERROR_STATUS_CODES = [
        STATUS_NOT_MODIFIED,
        STATUS_BAD_REQUEST,
        STATUS_UNAUTHORIZED,
        STATUS_NOT_FOUND,
        STATUS_CONFLIC,
        STATUS_METHOD_NOT_ALLOWED,
        STATUS_FORBIDDEN,
        STATUS_TOO_MANY_REQUESTS,
        STATUS_INTERNAL_SERVER_ERROR
    ] 
