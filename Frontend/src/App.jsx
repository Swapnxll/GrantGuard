import { Routes, Route, Navigate } from "react-router-dom";

import { useAuth } from "./context/AuthContext";

import FormPage from "./pages/FormPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";

export default function App() {
<<<<<<< HEAD
  const { isAuthenticated } = useAuth();
=======
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = async (formData) => {
    const loadingToast = toast.loading("Waking up GrantGuard AI agent...");

    try {
      // Ping backend
      await fetch("https://grantguard-g5p2.onrender.com");

      toast.success("Agent is online. Starting evaluation...", {
        id: loadingToast,
      });

      const response = await fetch(
        "https://grand-guard-server.onrender.com/evaluate",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        },
      );

      const data = await response.json();

      setResult(data);
      setShowModal(true);

      toast.success("Evaluation completed.");
    } catch (err) {
      toast.error("Unable to connect to GrantGuard.");
      console.error(err);
    }
  };
>>>>>>> be56c260164ccec48b574686381d233abff26d9b

  return (
    <Routes>
      {/* Protected Route */}
      <Route
        path="/"
        element={
          isAuthenticated ? <FormPage /> : <Navigate to="/login" replace />
        }
      />

      {/* Public Routes */}
      <Route
        path="/login"
        element={!isAuthenticated ? <LoginPage /> : <Navigate to="/" replace />}
      />

      <Route
        path="/register"
        element={
          !isAuthenticated ? <RegisterPage /> : <Navigate to="/" replace />
        }
      />

      {/* Catch all routes */}
      <Route
        path="*"
        element={<Navigate to={isAuthenticated ? "/" : "/login"} replace />}
      />
    </Routes>
  );
}
