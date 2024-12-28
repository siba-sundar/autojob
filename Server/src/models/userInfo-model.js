import mongoose, { Schema } from "mongoose";
import jwt from "jsonwebtoken";
import bcrypt from "bcrypt";

// Embedded Address Schema
const addressSchema = new Schema({
  houseNumber: {
    type: String,
    required: true,
  },
  city: {
    type: String,
    required: true,
  },
  state: {
    type: String,
    required: true,
  },
  pincode: {
    type: Number,
    required: true,
  },
});

// User Schema with Address as an embedded schema
const userSchema = new Schema(
  {
    fullName: {
      type: String,
      required: true,
    },
    phoneNumber: {
      type: String,
      required: true,
      trim: true,
    },
    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
      unique: true,
    },
    address: {
      type: addressSchema, // Embed Address schema
      required: true,
    },
    currentPosition: {
      type: String,
      required: false,
    },
    company: {
      type: String,
      required: false,
    },
    workExperience: {
      type: String,
      required: false,
    },
    highestDegree: {
      type: String,
      required: false,
    },
    university: {
      type: String,
      required: false,
    },
    graduationYear: {
      type: String,
      required: false,
    },
    technicalSkills: {
      type: String,
      required: false,
    },
    softSkills: {
      type: String,
      required: false,
    },
    linkedin: {
      type: String,
      required: false,
    },
    portfolio: {
      type: String,
      required: false,
    },
    languages: {
      type: String,
      required: false,
    },
    certifications: {
      type: String,
      required: false,
    },
    resume: {
      type: String, // Store the resume file path or URL
      required: true,
    },
    experienceType: {
      type: String,
      enum: ["fresher", "experienced"], // Only allow these values
      default: "fresher", // Default to fresher
    },
    keywords: {
      type: [String], // Array of strings to hold keywords like 'UI/UX'
      default: null,
    },
    location: {
      type: String, // Location string
      default: null,
    },
    paidOrUnpaid: {
      type: String,
      enum: ["paid", "unpaid"], // Only allow these values
      default: null,
    },
  },
  { timestamps: true }
);

export const User = mongoose.model("User", userSchema);
