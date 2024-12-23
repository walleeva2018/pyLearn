from django.shortcuts import render
from .forms import SignatureForm
from .models import Signature
import cv2
import numpy as np
from PIL import Image

def signature_verification(request):
    result = None
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            signature_instance = form.save()

            # Load original and signature images
            original_path = signature_instance.original_image.path
            signature_path = signature_instance.signature_image.path

            original = cv2.imread(original_path, 0)  # Grayscale
            signature = cv2.imread(signature_path, 0)  # Grayscale

            # Resize images for comparison
            signature = cv2.resize(signature, (original.shape[1], original.shape[0]))

            # Compute structural similarity
            from skimage.metrics import structural_similarity as compare_ssim
            score, _ = compare_ssim(original, signature, full=True)

            result = {
                "name": signature_instance.name,
                "score": round(score, 2),
                "match": score > 0.8  # Consider a match if similarity > 80%
            }
    else:
        form = SignatureForm()

    return render(request, 'signature/verify.html', {'form': form, 'result': result})
