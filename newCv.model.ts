import mongoose, { Schema, Document, Model } from "mongoose";

export type VerificationStatus = "pending" | "verified";

export interface IDuration {
  from: string;
  to: string;  
}

export interface IPersonal {
  fullName: string;
  email: string;
  phone: string;
  city: string;
  linkedin: string;
  github: string;
  summary: string;
  imgUrl?:string;
}

export interface IEducation {
  id: string;
  eduDocId: string;
  level: string;
  boardNameOrDegree: string;
  institutionName: string;
  gpa: string;
  duration: IDuration;
  selfAttested: boolean;
  docUri: string;
  issuerEmailId: string;
  isEmailSend: boolean;
  verified: boolean;
  status: VerificationStatus;
}

export interface IExperience {
  id: string;
  companyName: string;
  jobRole: string;
  duration: IDuration;
  skills: string;
  description: string;
  selfAttested: boolean;
  isEmailSend: boolean;
  docUri: string;
  issuerEmailId: string;
  verified: boolean;
  status: VerificationStatus;
}

export interface ISkill {
  id: string;
  skillName: string;
  level: string;
  selfAttested: boolean;
  endoresBy: string;
  endoresThrough: string;
}

export interface IProject {
  id: string;
  projectName: string;
  projectUrl: string;
  duration: IDuration;
  skills: string;
  description: string;
  selfAttested: boolean;
}

export interface IAward {
  id: string;
  level: string;
  name: string;
  organisation: string;
  duration: IDuration;
  description: string;
  selfAttested: boolean;
  issuerEmailId: string;
  docUri: string;
  isEmailSend: boolean;
  verified: boolean;
  status: VerificationStatus;
}

export interface ICv extends Document {
  userId:mongoose.ObjectId;
  title:string;
  personal: IPersonal;
  educations: IEducation[];
  experiences: IExperience[];
  skills: ISkill[];
  projects: IProject[];
  awards: IAward[];
}

// ---------- Sub-schemas ----------

const DurationSchema = new Schema<IDuration>(
  {
    from: { type: String, required: true },
    to: { type: String, default: "" },
  },
  { _id: false }
);

const PersonalSchema = new Schema<IPersonal>(
  {
    fullName: { type: String, required: true },
    email: { type: String, required: true },
    phone: { type: String, required: true },
    city: { type: String, required: true },
    linkedin: { type: String, required: false },
    github: { type: String, required: false },
    summary: { type: String, required: false },
    imgUrl:{type:String,required:false},
  },
  { _id: false }
);

const EducationSchema = new Schema<IEducation>(
  {
    id: { type: String, required: true },
    level: { type: String, required: true },
    boardNameOrDegree: { type: String, required: true },
    institutionName: { type: String, required: true },
    gpa: { type: String, required: true },
    duration: { type: DurationSchema, required: true },
    selfAttested: { type: Boolean, default: false },
    docUri: { type: String, default: "" },
    issuerEmailId: { type: String, default: "" },
    isEmailSend: { type: Boolean, default: false },
    verified: { type: Boolean, default: false },
    status: {
      type: String,
      enum: ["pending", "verified"],
      default: "pending",
    },
  },
  { _id: false }
);

const ExperienceSchema = new Schema<IExperience>(
  {
    id: { type: String, required: true },
    companyName: { type: String, required: true },
    jobRole: { type: String, required: true },
    duration: { type: DurationSchema, required: true },
    skills: { type: String, required: true },
    description: { type: String, default: "" },
    selfAttested: { type: Boolean, default: false },
    isEmailSend: { type: Boolean, default: false },
    docUri: { type: String, default: "" },
    issuerEmailId: { type: String, default: "" },
    verified: { type: Boolean, default: false },
    status: {
      type: String,
      enum: ["pending", "verified"],
      default: "pending",
    },
  },
  { _id: false }
);

const SkillSchema = new Schema<ISkill>(
  {
    id: { type: String, required: true },
    skillName: { type: String, required: true },
    level: { type: String, required: true },
    selfAttested: { type: Boolean, default: false },
    endoresBy: { type: String, default: "" },
    endoresThrough: { type: String, default: "" },
  },
  { _id: false }
);

const ProjectSchema = new Schema<IProject>(
  {
    id: { type: String, required: true },
    projectName: { type: String, required: true },
    projectUrl: { type: String, default: "" },
    duration: { type: DurationSchema, required: true },
    skills: { type: String, required: true },
    description: { type: String, default: "" },
    selfAttested: { type: Boolean, default: false },
  },
  { _id: false }
);

const AwardSchema = new Schema<IAward>(
  {
    id: { type: String, required: true },
    level: { type: String, required: true },
    name: { type: String, required: true },
    organisation: { type: String, required: true },
    duration: { type: DurationSchema, required: true },
    description: { type: String, default: "" },
    selfAttested: { type: Boolean, default: false },
    issuerEmailId: { type: String, default: "" },
    docUri: { type: String, default: "" },
    isEmailSend: { type: Boolean, default: false },
    verified: { type: Boolean, default: false },
    status: {
      type: String,
      enum: ["pending", "verified"],
      default: "pending",
    },
  },
  { _id: false }
);

// ---------- Root CV schema ----------

const CvSchema = new Schema<ICv>(
  {
    userId:{type:Schema.Types.ObjectId,ref:"TruCvUser",required:true,index:true},
    title:{type:String,required:true},
    personal: { type: PersonalSchema, required: true },
    educations: { type: [EducationSchema], default: [] },
    experiences: { type: [ExperienceSchema], default: [] },
    skills: { type: [SkillSchema], default: [] },
    projects: { type: [ProjectSchema], default: [] },
    awards: { type: [AwardSchema], default: [] },
  },
  {
    timestamps: true,
  }
);

export const UserCV: Model<ICv> =
  mongoose.models.UserCv || mongoose.model<ICv>("UserCv", CvSchema);
