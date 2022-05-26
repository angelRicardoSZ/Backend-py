from urllib import response
from django.urls import reverse
import datetime

from django.test import TestCase
from django.utils import timezone

from .models  import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently returns False for questions whose pub_date is in the future
        """
        time=timezone.now()+datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor CD?",pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        
    def test_was_published_recently_with_present_questions(self):
        """
        was_published_recently returns False for questions whose pub_date is more than 1 day in the past
        """
        time = timezone.now() - datetime.timedelta(days=1)
        recient_question = Question(question_text="¿Quien es el mejor X?",pub_date=time)
        self.assertIs(recient_question.was_published_recently(),True)
        
    def test_was_published_recently_with_old_questions(self):
        """
        was_published_recently returns False for questions whose pub_date is more than 1 day in the past
        """
        time = timezone.now() - datetime.timedelta(days=10)
        recient_question = Question(question_text="¿Quien es el mejor X?",pub_date=time)
        self.assertIs(recient_question.was_published_recently(),False)
        
        
def create_question(question_text,days):
    """
    Create a question with the given "question_text", 
    and publish the given number of days offset to now (negative
    for questions in the past)
    """
    time =timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)  
 
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no question exist, an appropiate message is displayed
        """
        response = self.client.get(reverse("polls:index"))
        self.assertAlmostEqual(response.status_code,200)        
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])
    def test_questions_with_future_pub_date(self):
        """
            Questions with a pub_date greater than the current date should not appear in the Index View.
        """
        create_question("Future Question", days=30)
        #Question(question_text='Present Question', pub_date=timezone.now()).save()
        #Question(question_text='Future Question', pub_date=timezone.now() + datetime.timedelta(days=30)).save()

        response = self.client.get(reverse('polls:index'))
        #self.assertEqual(response.status_code, 200)
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        #self.assertContains(response, "Present Question")
        #self.assertNotContains(response, "Future Question")    
        
    def test_questions_with_past_pub_date(self):
        """
            Questions with a pub_date in the past are displayed on the index page
        """
        question = create_question("Past Question", days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        
        
    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions are displayed
        """
        past_question = create_question(question_text="Past question", days=-30)
        future_question  = create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question]
            
        )
    
    def test_two_past_questions(self):
        """
        The question index page may display multiple questions.
        """
        past_question1 = create_question(question_text="Past question", days=-30)
        past_question2  = create_question(question_text="Future question", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1, past_question2]
            
        )
        
    def test_two_future_questions(self):
        future_question1 = create_question(question_text="Past question", days=30)
        future_question2 = create_question(question_text="Past question", days=30)
        
        response = self.client.get(reverse("polls:index"))
        
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            []
        )
        
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future    
        return a 404 error not found    
        """
        future_question = create_question(question_text="Future question", days=30)
        url = reverse("polls:detail",args=(future_question.id,))
        response =  self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_past_question(self):
        """
        The detail view of a questions with a pub_date in the past
        displays the question´s text       
        """
        past_question = create_question(question_text="Past question", days=-30)
        url = reverse("polls:detail",args=(past_question.id,))
        response =  self.client.get(url)
        self.assertContains(response, past_question.question_text)
        
        
    #def test_question_wo_answers(self):
    #    question = Question(question_text="test", pub_date=timezone.now())
    #    with self.assertRaises(Exception):
    #        question.save()



