from ..models import Emai


def add_emai(new_emai):
    emai = Emai(description=new_emai)
    emai.save()
    return emai.to_dict_json()


def list_email():
    email = Emai.objects.all()
    return [item.to_dict_json() for item in email]
