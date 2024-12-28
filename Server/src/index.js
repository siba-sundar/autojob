import dotenv from "dotenv";
import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import userRoutes from "./routes/user-route.js";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8000;
const DB_NAME = "jobautomation";

// Middleware
app.use(cors());
app.use(express.json());

// Database Connection
mongoose
  .connect(`mongodb://localhost:27017/${DB_NAME}`, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log(`MongoDB connected to ${DB_NAME}`))
  .catch((error) => {
    console.error("MongoDB connection error:", error);
    process.exit(1);
  });

// Routes
app.use("/api/users", userRoutes);

// Start Server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
