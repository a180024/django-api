from .models import File


def update_file(file: File, sensitivity_score: int) -> None:
    file.sensitivity_score = sensitivity_score
    file.flag = True
    file.save()




    
