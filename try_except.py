
==========================================
try except : example
==========================================

def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges_dictioinary[month]

        #sending html, f enables strong interpolation and can inject var
        response_data = f"<h1>{challenges_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Not supported</h1>")
