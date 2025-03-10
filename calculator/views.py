from django.shortcuts import render

def home(request):
  result = None
  
  if request.method == "POST":
    number1 = eval(request.POST.get("fist_number"))
    operation = request.POST.get("operation")
    number2 = eval(request.POST.get("second_number"))
    
    if operation == "addition":
      result = number1 + number2
      # print(result) for testing
      
    elif operation == "subtraction":
      result = number1 - number2
      # print(result) for testing
      
    elif operation == "multiplication":
      result = number1 * number2
      # print(result) for testing
      
    elif operation == "divition":
      result = number1 / number2
      # print(result) for testing
      
    else:
      result = "Invalid Input..."
    
    
  return render(request, "page/home.html", {"result": result})