import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";
import toast from "react-hot-toast";
import { useAuth } from "../context/AuthContext";

export default function LoginForm() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [loading, setLoading] = useState(false);

  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      // -----------------------------
      // Login
      // -----------------------------

      const response = await axios.post("http://localhost:8000/login", {
        // Backend expects "username"
        // We use the email as the username
        username: form.email,
        password: form.password,
      });

      console.log("Login response:", response.data);

      // -----------------------------
      // Get JWT
      // -----------------------------

      const token = response.data.access_token;

      if (!token) {
        throw new Error("No access token received");
      }

      // -----------------------------
      // Store JWT
      // -----------------------------

      login(token);

      // Also make sure it exists directly
      // in localStorage for App.jsx
      localStorage.setItem("token", token);

      // -----------------------------
      // Success
      // -----------------------------

      toast.success("Login successful!");

      navigate("/");
    } catch (err) {
      console.error("Login error:", err);

      const detail = err.response?.data?.detail;

      let errorMessage = "Invalid email or password";

      // FastAPI validation error
      if (Array.isArray(detail)) {
        errorMessage = detail[0]?.msg || "Invalid login details";
      }

      // FastAPI HTTPException
      else if (typeof detail === "string") {
        errorMessage = detail;
      }

      toast.error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md bg-white rounded-xl shadow-lg p-8">
      <h1 className="text-3xl font-bold mb-2">Welcome Back</h1>

      <p className="text-gray-500 mb-6">Login to your GrantGuard account.</p>

      <form onSubmit={handleSubmit} className="space-y-5">
        {/* Email */}

        <div>
          <label className="block mb-2 font-medium">Email</label>

          <input
            type="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
            placeholder="john@example.com"
            required
          />
        </div>

        {/* Password */}

        <div>
          <label className="block mb-2 font-medium">Password</label>

          <input
            type="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
            placeholder="********"
            required
          />
        </div>

        {/* Login */}

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-pink-500 text-white rounded-lg py-3 hover:bg-pink-600 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? "Logging in..." : "Login"}
        </button>
      </form>

      {/* Register */}

      <p className="text-center mt-6">
        Don't have an account?{" "}
        <Link
          to="/register"
          className="text-blue-600 font-semibold hover:underline"
        >
          Register
        </Link>
      </p>
    </div>
  );
}
