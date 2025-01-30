from django.shortcuts import render , get_object_or_404
from .models import Destination , Comments
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def index(request):
    
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

# @login_required
def details(request,id):
    dest = get_object_or_404(Destination,pk=id)
    
    if 'visited_destinations' not in request.session:
        request.session['visited_destinations'] = []

    if len(request.session['visited_destinations']) >= 2 and not request.user.is_authenticated:    
        messages.error(request, "Please login or register to access more destinations!")
        return render(request,'register.html')
        
       
    if id not in request.session['visited_destinations']:
        request.session['visited_destinations'].append(id)
        request.session.modified = True
                 
    all_comment = Comments.objects.filter(destination_name=dest)
    for comment in all_comment:
        comment.reply_count = comment.replies.count() 
    # total_comments = all_comment.count()    
    if request.method == 'POST':
        comment = request.POST['comment']
        parent_id = request.POST.get('parent_id') 
        if comment:
            parent_comment = None
            if parent_id:

                parent_comment = Comments.objects.get(id=parent_id) 

        comments = Comments.objects.create(comment=comment,user=request.user,destination_name=dest,parent=parent_comment)
        comments.save()
        return redirect('details',id=dest.id)

    return render(request,'details.html',{'dest':dest,'comments':all_comment})

@csrf_exempt
@login_required
def like_comment(request, comment_id):
    if request.method == 'POST':
        
        try:
            comment = Comments.objects.get(id=comment_id)
            # Assume a ManyToMany field or simple like count logic
            if request.user in comment.liked_users.all():
                comment.liked_users.remove(request.user)
                comment.like_count -= 1
                liked = False
            else:
                comment.liked_users.add(request.user)
                comment.like_count += 1
                liked = True
            comment.save()
            return JsonResponse({"success": True, "like_count": comment.like_count, "liked": liked})
        except Comments.DoesNotExist:
            return JsonResponse({"success": False, "error": "Comment not found"}, status=404)
    return JsonResponse({"success": False, "error": "Invalid request method"}, status=400)