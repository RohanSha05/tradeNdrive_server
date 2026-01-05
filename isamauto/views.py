import django
import json
import logging
import os
import platform
import requests
import rest_framework
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import success_response, error_response

logger = logging.getLogger(__name__)

@api_view(['GET'])
def server_info(request):
    """
    Return basic info about this API, using the standard response envelope.
    """
    try:
        info = {
            "title": "Isam Auto Backend",
            "django_version": django.get_version(),
            "drf_version": rest_framework.__version__,
            "python_version": platform.python_version(),
        }
        return success_response(info)
    except Exception as exc:
        return error_response(
            code=500,
            message=f"Failed to gather server info: {exc}",
            http_status=500
        )


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def hf_proxy(request, model):
    """Forward inference requests to Hugging Face Inference API with server-side token.

    The view expects the frontend to POST a JSON body containing the model inputs/params.
    It forwards that body to HF and returns the HF JSON response, adding permissive CORS
    headers so browsers can call it directly.
    """
    token = os.getenv("HF_TOKEN") or getattr(settings, "HF_TOKEN", None)
    logger.info(f"HF Proxy: model={model}, token_set={bool(token)}")
    
    if request.method == "OPTIONS":
        resp = JsonResponse({})
        resp["Access-Control-Allow-Origin"] = "*"
        resp["Access-Control-Allow-Headers"] = "*"
        resp["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return resp
    
    if not token:
        logger.error("HF_TOKEN is not configured")
        return JsonResponse({"error": "HF_TOKEN is not configured"}, status=500)

    # Preserve raw JSON; fallback to parsed data if body is empty
    payload = request.body if request.body else json.dumps(request.POST).encode()

    try:
        logger.info(f"Forwarding to HF: {model}")
        resp = requests.post(
            f"https://api-inference.huggingface.co/models/{model}",
            data=payload,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            timeout=120,
        )
        logger.info(f"HF Response: status={resp.status_code}")
        try:
            data = resp.json()
        except:
            data = {"error": resp.text, "status_code": resp.status_code}
            logger.warning(f"HF returned non-JSON: {resp.text[:200]}")
        proxied = JsonResponse(data, status=resp.status_code)
    except Exception as exc:
        logger.exception(f"Proxy error: {exc}")
        proxied = JsonResponse({"error": str(exc)}, status=500)

    # Permissive CORS for this proxy endpoint
    proxied["Access-Control-Allow-Origin"] = "*"
    proxied["Access-Control-Allow-Headers"] = "*"
    proxied["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return proxied