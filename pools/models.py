from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.TextField()
	closed = models.BooleanField(default = False)
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, null=True, related_name="choices")
	choice_text = models.CharField(max_length=255)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text + " " + str(self.votes) + " votes"