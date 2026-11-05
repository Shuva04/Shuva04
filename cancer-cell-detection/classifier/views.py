import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .model import predict

def home(request):
    return render(request, "index.html")

@require_POST
def predict_api(request):
    try:
        payload = json.loads(request.body or "{}")
        radius = float(payload["mean_radius"])
        texture = float(payload["mean_texture"])
        if not (0 < radius < 50 and 0 < texture < 60):
            raise ValueError("Values are outside the demo input range.")
        result = predict(radius, texture)
        return JsonResponse({
            **result,
            "notice": "Educational dataset demonstration only; not a medical diagnosis."
        })
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return JsonResponse({"error": str(exc)}, status=400)
