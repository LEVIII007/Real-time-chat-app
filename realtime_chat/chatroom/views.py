from django.shortcuts import render
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ChatRoomForm

@login_required
def room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chatroom = form.save(commit=False)
            chatroom.created_by = request.user
            chatroom.save()
    else:
        form = ChatRoomForm()

    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatroom/room.html', {'chatrooms': chatrooms, 'form': form})


@login_required

def chat(request, slug):
    room = get_object_or_404(ChatRoom, slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'chatroom/chat.html', {'room': room, 'messages': messages})