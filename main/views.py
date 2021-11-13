from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, Habits


def homepage(request):
    return render(request, "index.html")


def test(req):
    return render(req, "test.html", )


def test2(req):
    todo_list = ToDo.objects.all()
    return render(req, "test2.html", {"todo_list": todo_list})


def add_todo(req):
    form = req.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(test2)


def delete_todo(req, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test2)


def mark_todo(req, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test2)


def unmark_todo(req, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test2)

def done_todo(req,id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test2)


def to_meet(req):
    toMeet_list = ToMeet.objects.all()
    return render(req, 'meeting.html', {'toMeet_list': toMeet_list})


def meet_person(req):
    person_form = req.POST
    person_name = person_form['person_name']
    person_phone = person_form['person_phone']
    meeting = ToMeet(person=person_name, phone_number=person_phone)
    meeting.save()
    return redirect(to_meet)


def delete_meet(req, id):
    meet = ToMeet.objects.get(id=id)
    meet.delete()
    return redirect(to_meet)


def mark_meet(req, id):
    meet = ToMeet.objects.get(id=id)
    meet.is_favorite = True
    meet.save()
    return redirect(to_meet)


def unmark_meet(req, id):
    meet = ToMeet.objects.get(id=id)
    meet.is_favorite = False
    meet.save()
    return redirect(to_meet)


def habits(req):
    habits_text = Habits.objects.all()
    return render(req, 'habits.html', {'habits_text': habits_text})


def add_habits(req):
    habits_form = req.POST
    print(habits_form)
    habits_name = habits_form['habits_name']
    done_for_today = habits_form['done_for_today']
    comment = habits_form['comment']
    habits_all = Habits(habits_name=habits_name, done_for_today=done_for_today, comment=comment)
    habits_all.save()
    return redirect(habits)
