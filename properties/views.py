from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm

@login_required  
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)  
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.user = request.user 
            property_instance.save()  
            return redirect('property_list')  
    else:
        form = PropertyForm()

    return render(request, 'properties/add_property.html', {'form': form})
