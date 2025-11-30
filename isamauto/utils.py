from rest_framework.response import Response

def success_response(data, status=200):
    """
    Wrap a successful payload in the standard { data, error: None } envelope.
    """
    return Response({
        "data": data,
        "error": None
    }, status=status)

def error_response(code, message, http_status=None):
    """
    Wrap an error payload in the standard { data: None, error: { code, message } } envelope.
    """
    return Response({
        "data": None,
        "error": {
            "code": code,
            "message": message
        }
    }, status=http_status or code)