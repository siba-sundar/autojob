
import React, { useState } from 'react';
import axios from 'axios';
import Tesseract from 'tesseract.js';
import * as pdfjsLib from 'pdfjs-dist/webpack';

function ApplicationForm() {
  const [fullName, setFullName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [email, setEmail] = useState('');
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [state, setState] = useState('');
  const [currentPosition, setCurrentPosition] = useState('');
  const [company, setCompany] = useState('');
  const [workExperience, setWorkExperience] = useState('');
  const [highestDegree, setHighestDegree] = useState('');
  const [university, setUniversity] = useState('');
  const [graduationYear, setGraduationYear] = useState('');
  const [technicalSkills, setTechnicalSkills] = useState('');
  const [softSkills, setSoftSkills] = useState('');
  const [linkedin, setLinkedin] = useState('');
  const [portfolio, setPortfolio] = useState('');
  const [languages, setLanguages] = useState('');
  const [certifications, setCertifications] = useState('');
  const [resume, setResume] = useState(null);
  const [experienceType, setExperienceType] = useState('fresher');
  const [submitted, setSubmitted] = useState(false);

  const handleResumeChange = (e) => {
    setResume(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      fullName,
      phoneNumber,
      email,
      address,
      city,
      state,
      currentPosition,
      company,
      workExperience,
      highestDegree,
      university,
      graduationYear,
      technicalSkills,
      softSkills,
      linkedin,
      portfolio,
      languages,
      certifications,
      experienceType,
    };

    try {
      const response = await axios.post('http://localhost:8000/api/users', formData);
      console.log("User data saved successfully:", response.data);
      setSubmitted(true);
    } catch (error) {
      console.error("Error saving user data:", error);
    }
  };

  return (
    <div>
      <h2>Application Form</h2>
      {submitted && (
        <div>
          <h3>Submitted Information:</h3>
          <p><strong>Full Name:</strong> {fullName}</p>
          <p><strong>Phone Number:</strong> {phoneNumber}</p>
          <p><strong>Email:</strong> {email}</p>
          <p><strong>Address:</strong> {address}, {city}, {state}</p>
          <p><strong>Current Position:</strong> {currentPosition}</p>
          <p><strong>Company:</strong> {company}</p>
          <p><strong>Work Experience:</strong> {workExperience}</p>
          <p><strong>Highest Degree Earned:</strong> {highestDegree}</p>
          <p><strong>University/College:</strong> {university}</p>
          <p><strong>Graduation Year:</strong> {graduationYear}</p>
          <p><strong>Technical Skills:</strong> {technicalSkills}</p>
          <p><strong>Soft Skills:</strong> {softSkills}</p>
          <p><strong>LinkedIn Profile:</strong> {linkedin}</p>
          <p><strong>Portfolio/Website:</strong> {portfolio}</p>
          <p><strong>Languages Spoken:</strong> {languages}</p>
          <p><strong>Certifications:</strong> {certifications}</p>
          <p><strong>Resume:</strong> {resume ? resume.name : 'No resume uploaded'}</p>
        </div>
      )}
      {!submitted && (
        <form onSubmit={handleSubmit}>
          <h3>Basic Information</h3>
          <label>
            Full Name:
            <input type="text" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
          </label>

          <h3>Contact Information</h3>
          <label>
            Phone Number:
            <input type="tel" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} required />
          </label>
          <label>
            Email Address:
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </label>
          <label>
            Address:
            <input type="text" value={address} onChange={(e) => setAddress(e.target.value)} />
          </label>
          <label>
            City:
            <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
          </label>
          <label>
            State:
            <input type="text" value={state} onChange={(e) => setState(e.target.value)} />
          </label>

          <h3>Professional Information</h3>
          <label>
            Experience Level:
            <select value={experienceType} onChange={(e) => setExperienceType(e.target.value)}>
              <option value="fresher">Fresher</option>
              <option value="experienced">Experienced</option>
            </select>
          </label>

          {experienceType === 'experienced' && (
            <>
              <label>
                Current Position:
                <input type="text" value={currentPosition} onChange={(e) => setCurrentPosition(e.target.value)} />
              </label>
              <label>
                Company:
                <input type="text" value={company} onChange={(e) => setCompany(e.target.value)} />
              </label>
              <label>
                Work Experience:
                <textarea value={workExperience} onChange={(e) => setWorkExperience(e.target.value)} />
              </label>
            </>
          )}

          <h3>Education</h3>
          <label>
            Highest Degree Earned:
            <input type="text" value={highestDegree} onChange={(e) => setHighestDegree(e.target.value)} />
          </label>
          <label>
            University/College:
            <input type="text" value={university} onChange={(e) => setUniversity(e.target.value)} />
          </label>
          <label>
            Graduation Year:
            <input type="text" value={graduationYear} onChange={(e) => setGraduationYear(e.target.value)} />
          </label>

          <h3>Skills</h3>
          <label>
            Technical Skills:
            <textarea value={technicalSkills} onChange={(e) => setTechnicalSkills(e.target.value)} />
          </label>
          <label>
            Soft Skills:
            <textarea value={softSkills} onChange={(e) => setSoftSkills(e.target.value)} />
          </label>

          <h3>LinkedIn or Portfolio Links</h3>
          <label>
            LinkedIn Profile:
            <input type="url" value={linkedin} onChange={(e) => setLinkedin(e.target.value)} />
          </label>
          <label>
            Portfolio/Website:
            <input type="url" value={portfolio} onChange={(e) => setPortfolio(e.target.value)} />
          </label>

          <h3>Additional Information</h3>
          <label>
            Languages Spoken:
            <input type="text" value={languages} onChange={(e) => setLanguages(e.target.value)} />
          </label>
          <label>
            Certifications:
            <input type="text" value={certifications} onChange={(e) => setCertifications(e.target.value)} />
          </label>

          <h3>Upload Resume</h3>
          <label>
            Resume:
            <input type="file" accept=".pdf,.doc,.docx" onChange={(e) => setResume(e.target.files[0])} required />
          </label>

          <button type="submit">Submit</button>
        </form>
      )}
    </div>
  );
}

export default ApplicationForm;
