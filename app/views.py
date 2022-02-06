from uuid import UUID, uuid4
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from app.kdrama.kdrama import Kdrama
from typing import List

kdramas: List[Kdrama] = [
    Kdrama(id=uuid4(), moment="https://i.pinimg.com/236x/35/b9/40/35b940ad5fabd19b75ad6682d9944744.jpg", name="snowdrop", year="2021", remembered="나는 항상 당신을 기억할 것입니다"),
    Kdrama(id=uuid4(),moment="https://i.pinimg.com/236x/6a/34/18/6a341819fe042ea8325729dabe890d97.jpg", name="our beloved summer", year="2021", remembered="безответная любовь такое несчатье.."),
    Kdrama(id=uuid4(),moment="https://i.pinimg.com/236x/e4/4e/a8/e44ea8ff10f4764f2c2c4a172f14530f.jpg", name="kimetsy no yaiba", year="2019", remembered="какое же это счастье, когда ты не один.")

]



def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context={
        "kdramas": kdramas
    })

def delete(request: HttpRequest, id_: str) -> HttpResponse:
    global kdramas
    kdramas = [kdrama for kdrama in kdramas if kdrama.id != UUID(id_)]
    return HttpResponse("", status=204)


# def delete_form(request: HttpRequest, id_: str) -> HttpResponse:
#     global kdramas
#     if request.method == "POST":
#         cars = [kdrama for kdrama in kdramas if kdrama.id != UUID(id_)]
#         return HttpResponse("", status=204)
#     return redirect("/")
