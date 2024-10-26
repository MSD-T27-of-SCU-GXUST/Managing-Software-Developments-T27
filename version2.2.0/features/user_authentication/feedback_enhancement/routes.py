from flask import render_template, request, redirect, url_for, flash
from . import feedback_enhancement_bp
from ..models import Feedback
from .. import db

@feedback_enhancement_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_message = request.form.get('message')
        new_feedback = Feedback(name=user_name, message=user_message)

        db.session.add(new_feedback)
        db.session.commit()
        flash('反馈提交成功！')
        return redirect(url_for('feedback_enhancement.feedback'))

    feedbacks = Feedback.query.all()
    return render_template('enhanced_feedback.html', feedbacks=feedbacks)
