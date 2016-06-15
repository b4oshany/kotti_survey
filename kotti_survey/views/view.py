# -*- coding: utf-8 -*-

"""
Created on 2016-06-15
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_survey import _
from kotti_survey.resources import Survey, Question, AnswerField
from kotti_survey.fanstatic import css_and_js
from kotti_survey.views import BaseView


@view_defaults(context=Survey, permission="view")
class SurveyView(BaseView):
    """View for Survey Content Type"""

    @view_config(name="view",
                 request_method='GET',
                 renderer='kotti_survey:templates/surveyview.pt')
    def view_survey(self):
        return {}

    @view_config(name='view',
                 request_method='POST',
                 renderer='kotti_survey:templates/resultview.pt')
    def check_answers(self):
        questions = self.context.children
        answers = {question.name: self.request.POST.getall(
            question.name) for question in questions}
        self.context.save_answers(self.request, questions, answers)

        return {
            'questions': questions,
            'answers': answers
        }


@view_defaults(context=Question)
class QuestionView(BaseView):
    """View for Question Content Type"""

    @view_config(name="view", permission="view",
                 renderer='kotti_survey:templates/questionview.pt')
    def view_question(self):
        answers = self.context.values()
        return {
            'answers': answers,
        }


@view_defaults(context=AnswerField)
class AnswerView(BaseView):
    """View for Answer Content Type"""

    @view_config(name="view", permission="view",
                 renderer='kotti_quiz:templates/answerview.pt')
    def view_answer(self):
        return {}  # pragma: no cover
