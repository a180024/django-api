from celery import Task
from restapi.celery import app

from .models import File
from .services import update_file


class Sensitivity(Task):

    sensitivity = {
        'top-secret': 10,
        'secret': 7,
        'internal': 5,
        'external': 3,
        'public': 1
    }

    def get_words(self, file):
        """
        Read content from each file
        Return a list of words in lowercase
        """
        with file.open("r") as f:
            words = f.read().split()
            words = [word.lower() for word in words]
            return words
                
    def run(self):
        """
        Calculate the sensitivity score for each file
        """
        files = File.objects.all()
        for file in files:
            if not file.flag:
                words = self.get_words(file.file)
                sensitivity_score = sum([self.sensitivity.get(word, 0) for word in words])
                update_file(file, sensitivity_score)


app.register_task(Sensitivity())

            
            
            
