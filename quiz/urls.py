from django.urls import path
from quiz import views

urlpatterns = [
    path('',views.startQuiz,name="startQuiz"),
    path('quizInstruction/<str:slug>',views.quizInstruction,name="quizInstruction"),
    path('quizStart/<str:slug>',views.quizStart,name="quizStart"),
    path('handleQuiz',views.handleQuiz,name="handleQuiz"),
    path('viewAnswer/<int:id>',views.viewAnswer,name="viewAnswer"),
    path('quizScore/<int:id>',views.quizScore,name="quizScore"),
    path('category/<str:slug>',views.category,name="category"),
    path('viewScore/',views.viewScore,name="viewScore"),
    path('viewScore/<str:slug>',views.viewTitleScore,name="viewTitleScore"),
    path('feedback',views.feedback,name="feedback"),
    path('feedbackHandle',views.feedbackHandle,name="feedbackHandle"),
]
