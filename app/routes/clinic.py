from flask import Blueprint,  render_template, request, redirect
from models.clinic_models import Patient
from db import db


clinic = Blueprint('clinic', __name__)


@clinic.route('/clinics')
def clinics():
    patients = Patient.query.all()
    return render_template('clinics.html', patients=patients)


@clinic.route('/clinic_add', methods=['GET', 'POST'])
def clinic_add():
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']
        weight = float(request.form['weight'])
        age = float(request.form['age'])
        owner_name = request.form['owner_name']
        patient = Patient(name=name, details=details, weight=weight, age=age, owner_name=owner_name)
        db.session.add(patient)
        db.session.commit()
        return redirect('/clinics')
    return render_template('clinic_add.html')


@clinic.route('/clinic/edit/<int:id>', methods=['GET', 'POST'])
def clinic_edit(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.details = request.form['details']
        patient.weight = float(request.form['weight'])
        patient.age = float(request.form['age'])
        patient.owner_name = request.form['owner_name']
        db.session.commit()
        return redirect('/clinics')
    return render_template('clinic_edit.html', patient=patient)


@clinic.route('/clinic/delete/<int:id>', methods=['POST'])
def clinic_delete(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/clinics')