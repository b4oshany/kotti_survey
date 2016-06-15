# -*- coding: utf-8 -*-

"""
Created on 2016-06-15
:author: Oshane Bailey (b4.oshany@gmail.com)
"""
import uuid
from kotti import Base
from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Unicode,
    String,
    Boolean
)
from zope.interface import implements
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.dialects.postgresql import UUID

from kotti_survey import _


def uuid_factory():
    return uuid.uuid4()


class Survey(Content):
    """Survey Content type."""
    implements(IDefaultWorkflow)

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    collect_user_info = Column(Boolean, default=False)
    redirect_url = Column(String)

    def save_answers(self, request, questions, answers):
        for question in questions:
            if question.question_type == "text":
                if question.name in answers:
                    user_ans = answers[question.name][0]
                    if self.collect_user_info and request.user:
                        ans = UserAnswer(
                            answer=user_ans,
                            username=request.user.name,
                            question_id=question.id
                        )
                    else:
                        ans = UserAnswer(
                            answer=user_ans,
                            question_id=question.id
                        )
            else:
                answerchoice = question.children
                for answerchoice in answerchoices:
                    if question.question_type == "radio":
                        if question.name in answers:
                            user_ans = answers[question.name][0]
                            if self.collect_user_info and request.user:
                                ans = UserAnswer(
                                    answer=user_ans,
                                    username=request.user.name,
                                    question_id=question.id
                                )
                            else:
                                ans = UserAnswer(
                                    answer=user_ans,
                                    question_id=question.id
                                )
                    elif question.question_type == "checkbox":
                        if question.name in answers:
                            user_ans = ",".join(answers[question.name])
                            if self.collect_user_info and request.user:
                                ans = UserAnswer(
                                    answer=user_ans,
                                    username=request.user.name,
                                    question_id=question.id,
                                    is_multiple_choice=True
                                )
                            else:
                                ans = UserAnswer(
                                    answer=user_ans,
                                    question_id=question.id,
                                    is_multiple_choice=True
                                )

    type_info = Content.type_info.copy(
        name=u'Survey',
        title=_(u'Survey'),
        add_view=u'add_survey',
        addable_to=[u'Document'],
        )


class Question(Content):
    """Question Content type."""
    tablename = 'survey_questions'

    @declared_attr
    def __tablename__(cls):
        return cls.tablename

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    question_type = Column(String())

    # change the type info to your needs
    type_info = Content.type_info.copy(
        name=u'Question',
        title=_(u'Question'),
        add_view=u'add_question',
        addable_to=[u'Survey'],
        )


class AnswerField(Content):
    """Answer Content type."""

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Answer',
        title=_(u'Answer'),
        add_view=u'add_answer',
        addable_to=[u'Question'],
        )


class UserAnswer(Base):

    is_multiple_choice = Column(Boolean, default=False)
    userid = Column(Unicode(100), primary_key=True, default=uuid_factory())
    question_id = Column(Integer, ForeignKey('survey_questions.id'),
                         primary_key=True)
    answer = Column(String)
