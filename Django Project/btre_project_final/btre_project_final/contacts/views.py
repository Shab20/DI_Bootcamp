from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Contact

from django.shortcuts import get_object_or_404

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id', '')
        listing = request.POST.get('listing', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        user_id = request.POST.get('user_id', '')

        if not listing:
            messages.error(request, 'Missing required fields.')
            return redirect('index')

        # Check if user has already created an inquiry for this listing
        if request.user.is_authenticated:
            contact_exists = Contact.objects.filter(user_id=user_id, listing_id=listing_id).exists()
            if contact_exists:
                messages.warning(request, 'You have already submitted an inquiry for this listing.')
                return redirect('listing', listing_id=listing_id)

        # Create new instance of Contact model
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        messages.success(request, 'Your message has been sent!')

        return redirect('listing', listing_id=listing_id)

    else:
        return redirect('index')
