from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from app.models.user import db
from app.models.job import Job

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/jobs')
@login_required
def list_jobs():
    jobs = Job.query.all()
    return render_template('admin/jobs.html', jobs=jobs)

@admin_bp.route('/admin/jobs/add', methods=['GET', 'POST'])
@login_required
def add_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        job = Job(title=title, description=description)
        db.session.add(job)
        db.session.commit()
        flash('Job added successfully')
        return redirect(url_for('admin.list_jobs'))
    return render_template('admin/add_job.html')

