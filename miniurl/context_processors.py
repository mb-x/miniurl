from datetime import datetime


def get_infos(request):
    current_date = datetime.now()
    return {'current_date': current_date}