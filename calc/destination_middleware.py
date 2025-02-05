
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin
from .models import IPViewTracking
from .views import get_client_ip

class TrackUnauthenticatedViewsMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == 'details':
            if not request.user.is_authenticated:
                ip = get_client_ip(request)
                # Get or create a record for this IP address
                record, created = IPViewTracking.objects.get_or_create(ip_address=ip)
                
                destination_id = view_kwargs.get('id')
                
                if destination_id and destination_id not in record.viewed_destinations:
                    record.viewed_destinations.append(destination_id)
                    record.save()  # Save the updated record in the database
                
                # Check if more than 2 destinations have been viewed
                if len(record.viewed_destinations) > 2:
                    messages.info(request, 'Please register to view more destination details.')
                    return redirect('register')

        return None
