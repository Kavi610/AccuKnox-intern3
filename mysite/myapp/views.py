from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel
# Create your views here.
def create_instance(request):
    # Create an instance of MyModel
    obj = MyModel.objects.create(name="Original")

    # Print the name of the object before the transaction
    print("Name before save:", obj.name)  # This should be "Original"

    # Update the object within the same transaction
    obj.name = "Updated"
    obj.save()

    # Print the name of the object after the transaction
    print("Name after save:", obj.name)  # This should be "Updated"

    return HttpResponse("Instance created.")
