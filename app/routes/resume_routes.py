import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from app.utils.resume_parser import extract_text_from_pdf, extract_skills
from app.utils.job_recommender import recommend_jobs  # ✅ import this

resume_bp = Blueprint('resume', __name__)
UPLOAD_FOLDER = 'uploads'

@resume_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_resume():
    if request.method == 'POST':
        if 'resume' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['resume']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Extract text and skills
        text = extract_text_from_pdf(filepath)
        skills = extract_skills(text)

        # ✅ Recommend jobs
        jobs = recommend_jobs(skills)

        # Render skills + matched jobs
        return render_template('skills.html', skills=skills, jobs=jobs, name=current_user.email)

    return render_template('upload.html')
