import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";
import toast from "react-hot-toast";

export default function RegisterForm() {
  const navigate = useNavigate();

  const [loading, setLoading] = useState(false);

  const [form, setForm] = useState({
    email: "",
    phone_number: "",
    password: "",
    confirmPassword: "",
    email_notifications: true,
    sms_notifications: false,
  });

  const handleChange = (e) => {
    const { name, type, checked, value } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // -----------------------------
    // Validate password
    // -----------------------------

    if (form.password !== form.confirmPassword) {
      toast.error("Passwords do not match");
      return;
    }

    setLoading(true);

    try {
      // -----------------------------
      // Notification preferences
      // -----------------------------

      const selectedChannels = [];

      if (form.email_notifications) {
        selectedChannels.push("email");
      }

      if (form.sms_notifications) {
        selectedChannels.push("sms");
      }

      console.log("Selected channels:", selectedChannels);

      // -----------------------------
      // Register
      // -----------------------------
      // Backend expects:
      // {
      //   username: string,
      //   password: string
      // }
      //
      // We use the email as the username.

      const payload = {
        username: form.email,
        password: form.password,
      };

      console.log("Register payload:", {
        username: form.email,
      });

      const response = await axios.post(
        "http://localhost:8000/register",
        payload,
      );

      console.log("Register response:", response.data);

      toast.success("Registration successful!");

      navigate("/login");
    } catch (err) {
      console.error("Registration error:", err);

      const detail = err.response?.data?.detail;

      let errorMessage = "Registration failed";

      // FastAPI validation errors
      if (Array.isArray(detail)) {
        errorMessage = detail[0]?.msg || "Invalid registration data";
      }

      // Normal FastAPI HTTPException
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
      <h1 className="text-3xl font-bold mb-2">Create Account</h1>

      <p className="text-gray-500 mb-6">Register for GrantGuard.</p>

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

        {/* Confirm Password */}

        <div>
          <label className="block mb-2 font-medium">Confirm Password</label>

          <input
            type="password"
            name="confirmPassword"
            value={form.confirmPassword}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
            placeholder="********"
            required
          />
        </div>

        {/* Phone Number */}

        <div>
          <label className="block mb-2 font-medium">Phone Number</label>

          <input
            type="tel"
            name="phone_number"
            value={form.phone_number}
            onChange={handleChange}
            className="w-full border rounded-lg p-3"
            placeholder="0000000000"
            required
          />
        </div>

        {/* Register */}

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-pink-500 text-white rounded-lg py-3 hover:bg-pink-600 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? "Registering..." : "Register"}
        </button>
      </form>

      {/* Login */}

      <p className="text-center mt-6">
        Already have an account?{" "}
        <Link
          to="/login"
          className="text-blue-600 font-semibold hover:underline"
        >
          Login
        </Link>
      </p>
    </div>
  );
}
