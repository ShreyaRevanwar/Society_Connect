import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import base64
from django.utils import timezone
from datetime import timedelta
from .models import Captcha


def generate_captcha_text(length=6):
    """Generate random CAPTCHA text"""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))


def create_captcha_image(text):
    """Create a CAPTCHA image from text"""
    # Image dimensions
    width, height = 300, 100
    
    # Create image with dark background
    image = Image.new('RGB', (width, height), color='#0f1419')
    draw = ImageDraw.Draw(image)
    
    # Try to use a nice font, fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()
    
    # # Add noise lines
    # for _ in range(5):
    #     x1, y1 = random.randint(0, width), random.randint(0, height)
    #     x2, y2 = random.randint(0, width), random.randint(0, height)
    #     draw.line([(x1, y1), (x2, y2)], fill='#00d4ff', width=1)
    
    # # Add random dots
    # for _ in range(50):
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.point((x, y), fill='#00d4ff')
    
    # Add text with rotation
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, font=font, fill='#00d4ff')
    
    # # Apply slight filter
    # image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    return image


def image_to_base64(image):
    """Convert PIL Image to base64 string"""
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode()


def generate_and_store_captcha(session_key):
    """Generate CAPTCHA, store it, and return base64 image"""
    # Generate CAPTCHA text
    captcha_text = generate_captcha_text()
    
    # Create image
    captcha_image = create_captcha_image(captcha_text)
    
    # Convert to base64
    base64_image = image_to_base64(captcha_image)
    
    # Delete old CAPTCHA if exists
    Captcha.objects.filter(session_key=session_key).delete()
    
    # Store new CAPTCHA
    Captcha.objects.create(
        session_key=session_key,
        captcha_text=captcha_text.upper(),
        attempts=0
    )
    
    return base64_image


def verify_captcha(session_key, user_input):
    """Verify user's CAPTCHA input"""
    try:
        captcha = Captcha.objects.get(session_key=session_key)
        
        # Check if CAPTCHA has expired (5 minutes)
        if timezone.now() - captcha.created_at > timedelta(minutes=5):
            captcha.delete()
            return False, "CAPTCHA expired. Please refresh and try again."
        
        # Check attempts
        if captcha.attempts >= 3:
            captcha.delete()
            return False, "Too many attempts. Please refresh and try again."
        
        # Verify input
        if user_input.upper().strip() == captcha.captcha_text:
            captcha.delete()
            return True, "CAPTCHA verified successfully."
        else:
            captcha.attempts += 1
            captcha.save()
            remaining = 3 - captcha.attempts
            return False, f"Incorrect CAPTCHA. {remaining} attempts remaining."
    
    except Captcha.DoesNotExist:
        return False, "CAPTCHA not found. Please refresh the page."


def cleanup_old_captchas():
    """Delete CAPTCHA records older than 10 minutes"""
    cutoff_time = timezone.now() - timedelta(minutes=10)
    Captcha.objects.filter(created_at__lt=cutoff_time).delete()
