from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect;
from django.urls import reverse
# Create your views here.

# def january(request):
#      return HttpResponse("Take a cold🧊 shower🚿 everyday");

# def february(request):
#      return HttpResponse("Walk🚶🏽20 minutes everyday");



monthly_challenges_dict = {
    "january": "Take a cold🧊 shower🚿 everyday",
    "february": "Walk🚶🏽 20 minutes everyday",
    "march": "No🙅🏽 meat🍖 this month.",
    "april": "Read📖 10 pages of a book daily",
    "may": "No☕ caffeine☕ for 30 days",
    "june": "Wake up🌅 before 6 AM everyday",
    "july": "Write✍🏽 a journal🗒️ daily",
    "august": "Learn📚 one new thing everyday",
    "september": "Do📴 digital detox🧘🏽 every Sunday",
    "october": "Workout🏋🏽‍♂️ 4 times a week",
    "november": "Say🗣️ something nice to someone everyday",
    "december": "Reflect🪞 on the year and plan📝 next year"
}

def index(request):
     list_items=""
     months = list(monthly_challenges_dict.keys())
     
     for month in months:
          capitalized_month = month
          month_path = reverse("month-challenge",args=[month])
          list_items += f"<li>  <a href=\"{month_path}\">{capitalized_month}</a></li>"
     # loops khtm ho gya 
     response_data = f"<h1><ul>{list_items}</ul></h1>"
     return HttpResponse(response_data)






def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        back_to_index = reverse("index")  # Ye index page ka URL dega
        response_data = f"""
            <h1>{challenge_text}</h1>
            <br>
            <a href="{back_to_index}">
                <button style="padding: 10px; font-size: 16px;background-color:yellow">⬅️ Back to All Challenges</button>
            </a>
        """
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This Month is not found</h1>")

def monthly_challenge_by_number(request,month):
     months = list(monthly_challenges_dict.keys());
     if month > len(months) :
          return HttpResponseNotFound("Invalid Month");
     forward_month = months[month-1];
     redirect_path= reverse("month-challenge",args=[forward_month]) #/challenge/january
     # return HttpResponseRedirect("/challenges/"+forward_month);   
     return HttpResponseRedirect(redirect_path);

#     if month == 'january':
#         challenge_text = "Take a cold🧊 shower🚿 everyday"
#     elif month == 'february':
#         challenge_text = "Walk🚶🏽 20 minutes everyday"
#     elif month == 'march':
#         challenge_text = "No🙅🏽 meat🍖 this month."
#     elif month == 'april':
#         challenge_text = "Read📖 10 pages of a book daily"
#     elif month == 'may':
#         challenge_text = "No☕ caffeine☕ for 30 days"
#     elif month == 'june':
#         challenge_text = "Wake up🌅 before 6 AM everyday"
#     elif month == 'july':
#         challenge_text = "Write✍🏽 a journal🗒️ daily"
#     elif month == 'august':
#         challenge_text = "Learn📚 one new thing everyday"
#     elif month == 'september':
#         challenge_text = "Do📴 digital detox🧘🏽 every Sunday"
#     elif month == 'october':
#         challenge_text = "Workout🏋🏽‍♂️ 4 times a week"
#     elif month == 'november':
#         challenge_text = "Say🗣️ something nice to someone everyday"
#     elif month == 'december':
#         challenge_text = "Reflect🪞 on the year and plan📝 next year"
#     else:
#         return HttpResponseNotFound("This is an invalid month")

